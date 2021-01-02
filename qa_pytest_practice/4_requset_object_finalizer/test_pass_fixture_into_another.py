import pytest


@pytest.fixture()
def fixture_one():
    print("\n Im one")
    yield
    print("\n bye bye from fix one")


@pytest.fixture()
def fixture_two(fixture_one):
    print("\n Im two")
    yield
    print("\n bb from two")

def test_functuin(fixture_two):
    print("\n im a test func")