from api_for_test import *
import pytest


@pytest.fixture()
def good_code():
    return 200


@pytest.fixture()
def nod_found():
    return 404


def test_google_status_code(good_code):
    assert get_status_code("www.google.com") == good_code


def test_hackthebox_status_code(nod_found):
    assert get_status_code("www.hackthebox.eu") == nod_found


def test_codeby_status_code(good_code):
    assert get_status_code("www.codeby.net") == good_code


def test_cybersec_status_code(good_code):
    assert get_status_code("www.cybersec.org") == good_code


