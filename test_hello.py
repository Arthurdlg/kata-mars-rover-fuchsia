from hello import get_answer


def test_get_answer():
    actual = get_answer()
    assert actual == 42
