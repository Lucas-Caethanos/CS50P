from CS50P.Lecture_5_Unit_Tests.hello import hello


def test_argument():
    assert hello("David") == "hello, David"

    # Testing with loops
    # for name in ["Hermione", "Harry", "Ron"]:
    #     assert hello(name) == f"hello, {name}"


def test_default():
    assert hello() == "hello, world"
