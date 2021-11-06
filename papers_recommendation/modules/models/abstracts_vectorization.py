"""Module with abstracts vectorization"""

from typing import List, Optional

import scipy.sparse
from sklearn.feature_extraction.text import TfidfVectorizer


class AbstractVectorizationModel:
    def __init__(self):
        self.tfidf_vectorizer: TfidfVectorizer = TfidfVectorizer()

        self._corpus_sparse_vectors: Optional[scipy.sparse.csr_matrix] = None

    @property
    def corpus_sparse_vectors(self) -> scipy.sparse.csr_matrix:
        if self._corpus_sparse_vectors is None:
            raise ValueError('Abstract model is not trained yet')

        return self._corpus_sparse_vectors

    def train(self, corpus: List[str]) -> None:
        corpus_sparse_vectors = self.tfidf_vectorizer.fit_transform(
            raw_documents=corpus
        )
        self._corpus_sparse_vectors = corpus_sparse_vectors

    def get_vector(self, query: str) -> scipy.sparse.csr_matrix:
        if self._corpus_sparse_vectors is None:
            raise ValueError('Model is not trained yet')

        query_sparse_vector = self.tfidf_vectorizer.transform(raw_documents=[query])

        return query_sparse_vector
