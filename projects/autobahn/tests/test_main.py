from autobahn.main import main
from autobahn.main import pandas as pd
from autobahn.main import return_df

# import pandas as pd


def test_main():
    assert main() == "I am autobahn"


def test_return_df():
    df = return_df()
    assert df.shape == (3, 2)
    assert isinstance(df, pd.DataFrame)
    pd.testing.assert_frame_equal(df, pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}))
