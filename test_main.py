from project import get, open_txt, random_pick, write_txt
import pytest
    from pathlib import Path

def test_get():
    assert get(["-n", "m.txt"]) == "m.txt"
    with pytest.raises(ValueError):
        assert get(["-n", "m"])
        assert get(["-n", ""])


def test_open_txt():
    with pytest.raises(ValueError):
        assert open_txt("nonexisting.txt")


def test_random_pick():
    q = [{"N": 0, "Q": "Why"},{"N": 1, "Q": "Why is"},{"N": 2, "Q": "Why is is"}]
    n = 2
    assert len(random_pick(n, q)) == 2

def test_write_txt():
    q = [{"N": 0, "Q": "Why"},{"N": 1, "Q": "Why is"},{"N": 2, "Q": "Why is is"}]
    write_txt(q,"q.txt")
    path_to_file = "q.txt"
    path = Path(path_to_file)
    assert path.is_file() == True
