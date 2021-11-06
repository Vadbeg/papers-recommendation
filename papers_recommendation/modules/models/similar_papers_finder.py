"""Module with model for finding similar papers"""

from typing import List, Union
from pathlib import Path

import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA

from papers_recommendation.modules.models.titles_vectorization import (
    TitlesVectorizationModel
)
from papers_recommendation.modules.models.abstracts_vectorization import (
    AbstractVectorizationModel
)
from papers_recommendation.modules.data.code_paper import CodePaper


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
        
    def train_abstract_model(self):
        corpus = [curr_paper.abstract for curr_paper in self._papers]
        self._abstract_vectorization_model.train(corpus=corpus)
        
    def train_nearest_neighbours_model(self):
        vectors = self._get_papers_vectors()
        
        self._nearest_neighbours_model.fit(X=vectors)
        
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
        sparse_abs_vectors = self._abstract_vectorization_model.corpus_sparse_vectors
        abs_vectors = sparse_abs_vectors.toarray()

        n_components = min(abs_vectors.shape[0], abs_vectors.shape[1], 300)
        abs_vectors = PCA(n_components=n_components).fit_transform(X=abs_vectors)
    
        return abs_vectors
    

