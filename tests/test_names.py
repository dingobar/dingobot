import pytest

from namegen import NameGenerator, name_endings


@pytest.fixture
def namegen():
    return NameGenerator()


def test_get_fullname(namegen: NameGenerator):
    name = namegen.get_fullname()
    assert isinstance(name, str)
    names = name.split(" ")
    assert any(n[0].isupper() for n in names)
    assert len(names) > 1


def test_get_name(namegen: NameGenerator):
    name = namegen.get_name()
    assert name[0].isupper()


def test_get_lastname(namegen: NameGenerator):
    name = namegen.get_lastname()
    assert any(name.endswith(ending) for ending in name_endings)
