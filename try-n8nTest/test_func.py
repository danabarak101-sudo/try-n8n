from main import add, sub, multiple
import pytest

def test_run(request):
    machine_name = request.config.getoption("--mname")
    version = request.config.getoption("--mver")
    user = request.config.getoption("--muser")
    password = request.config.getoption("--mpass")

    print(f"VM: {machine_name}, Version: {version}, User: {user}, Password: {password}")

    assert machine_name is not None
    assert version is not None

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (1.5, 2.5, 4.0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (0, 5, -5),
    (-1, -1, 0)
])
def test_sub(a, b, expected):
    assert sub(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (5, 0, 0),
    (-2, 3, -6),
    (-2, -2, 4)
])
def test_multiple(a, b, expected):
    assert multiple(a, b) == expected

def test_add_strings():
    assert add("hello ", "world") == "hello world"
