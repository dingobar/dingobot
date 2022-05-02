import pytest
from eurovision import message_is_about_eurovision, time_until_eurovision


def test_time_until_esc() -> None:
    time_until_esc = time_until_eurovision()
    assert isinstance(time_until_esc, str)


@pytest.mark.parametrize(
    "input,expected",
    [
        ("This is about Eurovision!", True),
        ("So is this message about mgp.", True),
        ("This is unrelated", False),
    ],
)
def test_message_is_about_eurovision(input, expected) -> None:
    assert message_is_about_eurovision(input) == expected
