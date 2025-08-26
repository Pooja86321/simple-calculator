from fastapi import FastAPI
app = FastAPI()
@app.get("/multiply")
def multiply(a:int, b:int):
    return {
        "multiply": a*b
        }
@app.get("/addition")
def addition(a: int, b: int):
    return {"addtion": a + b}

@app.get("/subtraction")
def subtraction(a: int, b: int):
    return {"subtraction": a - b}

@app.get("/division")
def division(a: int, b: int):
    return {"addtion": a / b}
