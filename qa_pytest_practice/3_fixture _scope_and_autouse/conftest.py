import pytest


@pytest.fixture(scope="class")
def class_fixture():
    print("Class Fix")

@pytest.fixture(scope="module")
def module_fixture():
    print("Module_fix here")


@pytest.fixture(scope="session")
def session_fixture():
    print("Seesion fix")


@pytest.fixture(autouse=True)
def auto_use_fix():
    print("AUTOUSEE")