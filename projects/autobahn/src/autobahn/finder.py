import os
from typing import List


def find_files(files: list[str], pattern: str) -> list[str]:
    # find files that match the pattern
    return [f for f in files if f.endswith(pattern)]
