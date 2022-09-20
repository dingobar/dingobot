from pydantic import BaseModel
import wikipedia


wikipedia.set_lang("no")


class NameEtymologyPart(BaseModel):
    part_name: str
    meaning: str
    summary: str


class NameEtymology(BaseModel):
    name: str
    parts: list[NameEtymologyPart]


def _get_random_wikipage() -> str:
    return wikipedia.random()


def _search_wikipedia(term: str) -> str:
    """Wow recursion! Much clever! Such programming!"""
    results = wikipedia.search(term)
    if len(results) > 0:
        return results[0]
    else:
        return _get_random_wikipage()


def _get_wikipedia_summary(title) -> str:
    try:
        return wikipedia.summary(title, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return _get_wikipedia_summary(e.options[0])


def _name_to_parts(name) -> list[list[str]]:
    parts = name.split(" ")
    final_parts = []
    for part in parts:
        if (pl := len(part)) > 5:
            middle_index = pl // 2
            final_parts.append([part[:middle_index], part[middle_index:]])
        elif len(part) < 3:
            pass
        else:
            final_parts.append([part])
    return final_parts


def get_etymology(name) -> list[NameEtymology]:
    names = _name_to_parts(name)
    name_meanings = []
    for name_part in names:
        part_meanings = []
        for part in name_part:
            part_meaning = _search_wikipedia(part)
            part_meanings.append(
                NameEtymologyPart(
                    part_name=part,
                    meaning=part_meaning,
                    summary=_get_wikipedia_summary(part_meaning),
                )
            )
        name_meanings.append(NameEtymology(name="".join(name_part), parts=part_meanings))
    return name_meanings
