import pandas as pd
import logging

logger = logging.getLogger(__name__)

def main():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    logger.info(f"I rely on pandas now:\n {df}")
    return "i am ddd"
