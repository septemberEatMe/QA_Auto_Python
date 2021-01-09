import pytest


@pytest.mark.parametrize("test_input", [1, 2, 3])
class TestClassParametrized:

    def test_one(self, test_input):
        pass

    def test_two(self, test_input):
        print(f" test no.{test_input} params = {test_input}")
