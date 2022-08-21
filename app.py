from fastapi import FastAPI

from dingobot.namegen import NameGenerator

app = FastAPI()


@app.get("/v1/names")
def read_root(n: int = 1):
    names = []
    for _ in range(n):
        namegen = NameGenerator()
        names.append(namegen.get_fullname())
    return names
