"""A small FastAPI service for adding two numbers."""

import math

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, FiniteFloat

app = FastAPI(title="Addition API", version="1.0.0")


class AdditionRequest(BaseModel):
    a: FiniteFloat
    b: FiniteFloat


class AdditionResponse(BaseModel):
    result: FiniteFloat


@app.post("/add", response_model=AdditionResponse)
def add_numbers(numbers: AdditionRequest) -> AdditionResponse:
    """Add two finite numbers and return their sum."""
    result = numbers.a + numbers.b
    if not math.isfinite(result):
        raise HTTPException(status_code=422, detail="The sum is outside the supported range.")
    return AdditionResponse(result=result)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
