from fastapi import FastAPI

app : FastAPI = FastAPI()

@app.get('/')
def message():
    return '🚀'