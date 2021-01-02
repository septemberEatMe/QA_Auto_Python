import pytest


@pytest.fixture()
def fixture_info(request):
    print("\n-------------")
    print(f"{request.node}")
    print(f"{request.scope}")
    print(f"{request.cls}")
    print(f"{request.module}")
    print("-------------")


def test_one(fixture_info):
    print("\n Test one fix request obj")


class TestClass:

    def test_one(self, fixture_info):
        print("TestClass func one from folder 4 ")