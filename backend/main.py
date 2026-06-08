from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sumar")
def sumar(a: float, b: float):
    return {"resultado": a + b}

@app.get("/restar")
def restar(a: float, b: float):
    return {"resultado": a - b}