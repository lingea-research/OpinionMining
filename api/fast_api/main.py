from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn

from constants import VERSION


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Version(BaseModel):
    version: str


class OpinionMiningInput(BaseModel):
    language: str
    full_text: str


class OpinionMiningOutputTriple(BaseModel):
    what: str  # what topic is being evaluated
    how: str   # how is it evaluated, for example, pos, neg, neu
    why: str   # why is it evaluated that way


class OpinionMiningOutput(BaseModel):
    triples: List[OpinionMiningOutputTriple]


@app.get("/")
async def root() -> Version:
    return Version(
        version=VERSION
    )


@app.post("/opinion_mining")
async def opinion_mining(input: OpinionMiningInput) -> OpinionMiningOutput:
    return OpinionMiningOutput(
        triples=
        [
            OpinionMiningOutputTriple(
                what="aaa", how="bbb", why="ccc"
            ),
            OpinionMiningOutputTriple(
                what="111", how="222", why="333"
            )
        ]
    )


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=4999)
