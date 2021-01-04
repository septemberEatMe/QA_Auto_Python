import pytest


@pytest.fixture()
def print_info_about_test(request):
    print("\n-------------------")
    print(f"{request.node}")
    print(f"{request.scope}")
    print(f"{request.cls}")
    print(f"{request.module}")
    print("\n-------------------")


def return_int():
    return 5


def sum_two_numbers(num_one, num_two):
    return num_one + num_two


def say_hello(name):
    print(f"Hello, {name}")


def get_even_nums(numbers):
    return [x for x in numbers if x % 2 == 0]


def get_first_element_from_tuple(countries):
    print(countries[0])

def test_int_type(print_info_about_test):
    assert type(return_int()) == int


def test_sum(print_info_about_test):
    assert sum_two_numbers(5, 5) == 10


def test_say_hello(print_info_about_test):
    assert say_hello("Alex") == print("Hello, Alex")


def test_get_even_nums(print_info_about_test):
    numbers = [1, 4, 77, 3, 24, 65]
    assert get_even_nums(numbers) == [4, 24]


def test_get_first_elem_form_tuple():
    countries = ("usa", "bra", "ita")
    assert get_first_element_from_tuple(countries) == print("usa")