import logging
import os

import pandas as pd
from autobahn.finder import find_files

logger = logging.getLogger(__name__)


def main():
    files = os.listdir(".")
    python_files = find_files(files, ".py")
    logger.info(python_files)
    return "I am autobahn"


def return_df() -> pd.DataFrame:
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    logger.info(df)
    return df
