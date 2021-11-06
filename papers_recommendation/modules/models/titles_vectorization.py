"""Module with titles vectorization"""

from pathlib import Path
from typing import Union

import fasttext
import fasttext.util
import numpy as np


class TitlesVectorizationModel:
    def __init__(self, model_path: Union[str, Path]):
        self._model = self._load_model(model_path=Path(model_path).absolute())

    def get_vector(self, text: str) -> np.ndarray:
        sentence_vector = self._model.get_sentence_vector(text=text)

        return sentence_vector

    @staticmethod
    def _load_model(model_path: Path) -> fasttext.FastText:
        if not model_path.exists():
            raise ValueError(f'No model in given path: {model_path}')

        model: fasttext.FastText = fasttext.load_model(path=str(model_path))

        return model
