import pytest
#Fixture uses when need db connect and избыточный код
@pytest.fixture
def first_fixtuer():
    print("\n Fixture here")

def test_one(first_fixtuer):
    pass

def test_two(first_fixtuer):
    pass

class ClassTest():

    def test_one(self, first_fixtuer):
        pass

    def test_two(self, first_fixtuer):
        pass