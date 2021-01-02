


def test_the_number(fixture_return_rnd_value):
    assert fixture_return_rnd_value == 20


def test_return_class(fixture_return_class):
    assert fixture_return_class.hello("Alex") == "Hello, Alex"