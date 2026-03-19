from main import add, sub, multiple
import pytest
import pytest

# טסט לפונקציית החיבור
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (1.5, 2.5, 4.0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# טסט לפונקציית החיסור
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (0, 5, -5),
    (-1, -1, 0)
])
def test_sub(a, b, expected):
    assert sub(a, b) == expected

# טסט לפונקציית הכפל
@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (5, 0, 0),
    (-2, 3, -6),
    (-2, -2, 4)
])
def test_multiple(a, b, expected):
    assert multiple(a, b) == expected


# דוגמה לטסט שבודק סוג נתונים (אופציונלי)
def test_add_strings():
    # בפיpython חיבור מחרוזות מבצע שרשור
    assert add("hello ", "world") == "hello world"
