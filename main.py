from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return "Hello World"

@app.get("/data")
def json():
    return {
        "name": "Smriti Jopat",
        "Company": "NPCI"
    }