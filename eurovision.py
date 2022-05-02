import arrow
from humanize import precisedelta, activate

STARTTIME = arrow.get("2022-05-10T21:00:00+02:00")

EUROVISION_SLUGS = [
    "eurovision",
    "mgp",
    "esc",
    "melodi grand prix",
    "tix",
    "subwoolfer",
]


def time_until_eurovision() -> str:
    activate("da_DK")
    now = arrow.utcnow().to("Europe/Rome")
    difference = STARTTIME - now
    return precisedelta(difference)


def message_is_about_eurovision(msg: str) -> bool:
    return any((slug.lower() in msg.lower() for slug in EUROVISION_SLUGS))
