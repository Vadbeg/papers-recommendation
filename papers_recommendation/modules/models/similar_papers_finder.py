"""Module with model for finding similar papers"""

from pathlib import Path
from typing import List, Tuple, Union

import numpy as np
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors

from papers_recommendation.modules.data.code_paper import CodePaper
from papers_recommendation.modules.models.abstracts_vectorization import (
    AbstractVectorizationModel,
)
from papers_recommendation.modules.models.titles_vectorization import (
    TitlesVectorizationModel,
)


class SimilarPapersFinder:
    def __init__(
        self, papers: List[CodePaper], titles_model_path: Union[Path, str]
    ) -> None:
        self._papers = papers

        self._titles_vectorization_model = TitlesVectorizationModel(
            model_path=titles_model_path
        )
        self._abstract_vectorization_model = AbstractVectorizationModel()

        self._nearest_neighbours_model = NearestNeighbors()
        self._pca = PCA()

    def train_abstract_model(self):
        corpus = [curr_paper.abstract for curr_paper in self._papers]
        self._abstract_vectorization_model.train(corpus=corpus)

    def train_nearest_neighbours_model(self):
        vectors = self._get_papers_vectors()

        self._nearest_neighbours_model.fit(X=vectors)

    def get_nearest_papers(
        self, paper: CodePaper, n_nearest: int = 5
    ) -> List[Tuple[int, float]]:
        title_vector = self._titles_vectorization_model.get_vector(text=paper.title)
        title_vector = title_vector[np.newaxis, :]

        abstract_vector = self._abstract_vectorization_model.get_vector(
            query=paper.abstract
        )
        abstract_vector = self._pca.transform(X=abstract_vector)

        vector = np.concatenate((title_vector, abstract_vector), axis=1)

        result = self._nearest_neighbours_model.kneighbors(
            X=vector, n_neighbors=n_nearest
        )
        items = self._postprocess_knn_pred(knn_pred=result)

        return items

    @staticmethod
    def _postprocess_knn_pred(
        knn_pred: Tuple[np.ndarray, np.ndarray]
    ) -> List[Tuple[int, float]]:
        distances = knn_pred[0][0].tolist()
        papers_ids = knn_pred[1][0].tolist()

        items = [
            (curr_paper_id, curr_distance)
            for curr_paper_id, curr_distance in zip(papers_ids, distances)
        ]

        return items

    def _get_papers_vectors(self) -> np.ndarray:
        titles_vectors = self._get_all_titles_vectors()
        abstracts_vectors = self._get_all_abstract_vectors()

        vectors = np.concatenate((titles_vectors, abstracts_vectors), axis=1)

        return vectors

    def _get_all_titles_vectors(self) -> np.ndarray:
        titles_vectors = [
            self._titles_vectorization_model.get_vector(text=curr_paper.title)
            for curr_paper in self._papers
        ]

        return np.array(titles_vectors)

    def _get_all_abstract_vectors(self) -> np.ndarray:
        abs_vectors = self._abstract_vectorization_model.corpus_sparse_vectors

        n_components = min(abs_vectors.shape[0], abs_vectors.shape[1], 300)
        self._pca.n_components = n_components

        abs_vectors = self._pca.fit_transform(X=abs_vectors)

        return abs_vectors
