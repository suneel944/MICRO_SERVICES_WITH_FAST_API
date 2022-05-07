from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"test": "I am god"}