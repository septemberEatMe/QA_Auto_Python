import pytest


#Fixture uses when need db connect and избыточный код
#@pytest.fixture
#def first_fixture():
#   print("\n Fixture here")


def test_one(first_fixture):
    pass


def test_two(first_fixture):
    pass


class ClassTest():

    def test_one(self, first_fixture):
        pass

    def test_two(self, first_fixture):
        pass