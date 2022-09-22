from os import environ
from typing import List

from fastapi import FastAPI, HTTPException
from mangum import Mangum
from pydantic import BaseModel

from dingobot.etymology import NameEtymology, get_etymology
from dingobot.eurovision import time_until_eurovision
from dingobot.namegen import generate_names

stage = environ.get("STAGE")
root_path = f"/{stage}" if stage else "/"
app = FastAPI(title="dingobot", root_path="/Prod")


@app.get(
    "/v1/names",
    tags=["Norske Navn"],
    description="Autogenererte norske navn til 20 i stil",
    response_model=List[str],
)
def names(n: int = 1):
    if n < 1 or n > 1000:
        raise HTTPException(
            status_code=400, detail=f"n must be in range [1, 1000], got {n}"
        )
    return generate_names(n)


class CountdownValue(BaseModel):
    time_until_eurovision: str


@app.get("/v1/eurovision/countdown", tags=["Eurovision"], response_model=CountdownValue)
def eurovision_countdown():
    return CountdownValue(time_until_eurovision=time_until_eurovision())


@app.get(
    "/v1/names/{name}/etymology",
    tags=["Norske Navn"],
    description="Lurer du på hva navnet ditt betyr?",
    response_model=list[NameEtymology],
)
def name_etymology(name: str) -> list[NameEtymology]:
    if len(name) > 30:
        raise HTTPException(
            status_code=400, detail="The name is too long - limit to 30 characters max"
        )

    return get_etymology(name)


handler = Mangum(app)
