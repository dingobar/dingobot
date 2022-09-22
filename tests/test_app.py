import pytest
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


@pytest.mark.parametrize("n", range(1, 1000, 99))
def test_when_n_then_names(n):
    response = client.get("/v1/names", params={"n": n}).json()
    assert len(response) == n


@pytest.mark.parametrize(
    "n, code", [(1, 200), (1000, 200), (0, 400), (-500, 400), (10000, 400)]
)
def test_when_invalid_n_then_400(n, code):
    status_code = client.get("/v1/names", params={"n": n}).status_code
    assert status_code == code
