import pytest


@pytest.mark.parametrize("test_input, excepted", [("2 + 3", 5), ("2 + 2", 4), ("1 + 14", 15)])

def test_parametrize_with_mark_add(test_input, excepted):
    assert eval(test_input) == excepted