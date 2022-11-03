from autobahn.finder import find_files


def test_find_files():
    files = ["a.py", "b.py", "c.py", "d.txt", "e.txt", "f.txt"]
    actual = find_files(files, ".py")
    expected = ["a.py", "b.py", "c.py"]
    assert actual == expected
