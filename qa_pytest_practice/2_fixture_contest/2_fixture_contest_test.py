import pytest


def test_global_fixture(confest_fixture):
    pass


class TestClass:

    def test_one(self, global_fixture):
        pass
