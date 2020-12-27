import pytest


@pytest.fixture
def global_fixture():
    print("\n Global Fixture")
