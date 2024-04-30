from fastapi import FastAPI

app = FastAPI()

@app.get('/we')
def welcome():
    return {
        "masseage":"welcome ya pro"
    }
