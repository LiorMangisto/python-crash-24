import pytest

@pytest.fixture()
def setup_teardown():
    print("\nBefore Test") # Before test
    yield # Here test is executed
    print("\nTacking screenshot") # After test
    print("Tacking Logs") # After test

def test_demo_1():
    assert 1 == 1


def test_demo_2(setup_teardown):
    print("\nTesting!")
    assert 2 > 1

