import pytest


@pytest.fixture(params=[1, 2, 3, 4])
def fixture_with_params(request):
    return request.param

