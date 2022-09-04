from typing import List
from fastapi import FastAPI, HTTPException
from mangum import Mangum
from pydantic import BaseModel

from dingobot.namegen import generate_names
from dingobot.eurovision import time_until_eurovision

stage = "Prod"  # How can I infer it from the environment
root_path = f"/{stage}" if stage else "/"
app = FastAPI(title="dingobot", root_path=root_path)


@app.get(
    "/v1/names",
    tags=["Norske Navn"],
    description="Autogenererte norske navn til 20 i stil",
    response_model=List[str],
)
def names(n: int = 1):
    if n < 1 or n > 1000:
        raise HTTPException(status_code=400, detail=f"n must be in range [1, 1000], got {n}")
    return generate_names(n)


class CountdownValue(BaseModel):
    time_until_eurovision: str


@app.get("/v1/eurovision/countdown", tags=["Eurovision"], response_model=CountdownValue)
def eurovision_countdown():
    return CountdownValue(time_until_eurovision=time_until_eurovision())


handler = Mangum(app)