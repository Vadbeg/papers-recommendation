"""Module with abstracts vectorization"""

from typing import List, Optional

import numpy as np
import scipy.sparse
from sklearn.feature_extraction.text import TfidfVectorizer


class AbstractVectorizationModel:
    def __init__(self):
        self.tfidf_vectorizer: TfidfVectorizer = TfidfVectorizer()

        self._corpus_vectors: Optional[np.ndarray] = None

    @property
    def corpus_sparse_vectors(self) -> np.ndarray:
        if self._corpus_vectors is None:
            raise ValueError('Abstract model is not trained yet')

        return self._corpus_vectors

    def train(self, corpus: List[str]) -> None:
        corpus_sparse_vectors = self.tfidf_vectorizer.fit_transform(
            raw_documents=corpus
        )
        self._corpus_vectors = corpus_sparse_vectors.toarray()

    def get_vector(self, query: str) -> np.ndarray:
        if self._corpus_vectors is None:
            raise ValueError('Model is not trained yet')

        query_sparse_vector = self.tfidf_vectorizer.transform(raw_documents=[query])
        query_vector = query_sparse_vector.toarray()

        return query_vector
