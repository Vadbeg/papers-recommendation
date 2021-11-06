"""Module with utils for CLI"""

import pickle
from pathlib import Path
from typing import Any, Union


def pickle_save(obj: Any, path: Union[str, Path]) -> None:
    path = Path(path)
    with path.open(mode='wb') as file:
        pickle.dump(obj=obj, file=file)


def pickle_load(path: Union[str, Path]) -> Any:
    path = Path(path)
    with path.open(mode='rb') as file:
        obj = pickle.load(file=file)

    return obj
