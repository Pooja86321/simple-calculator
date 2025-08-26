from fastapi import FastAPI
app = FastAPI()
@app.get("/calc")
def calc(a:int, b:int):
    return {
        "add": a+b,
        "sub":a-b,
        "multiply": a*b,
        "div": a/b
        }

