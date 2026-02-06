import ci_course


def test_greet():
    """
    Test the function `greet` in functionality.py
    """
    assert ci_course.greet() == "Hello "
    assert ci_course.greet("Fergus") == "Hello Fergus"


def test_minimum():
    """
    Test the function `minimum` in functionality.py
    """
    assert ci_course.minimum(1, 2, 3) == 1
    assert ci_course.minimum(1.2, 2.3) == 1.2
    assert ci_course.minimum(-1.2, -3) == -3
    assert ci_course.minimum(2, "skip me", 1) == 1
    assert ci_course.minimum('hi', 'you') is None


def test_minimum_no_args_returns_none():
    """
    Ensure the `minimum` early-return path is covered.
    """
    assert ci_course.minimum() is None
