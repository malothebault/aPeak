from fastapi import FastAPI
from datetime import datetime
import json

app = FastAPI()


@app.get('/note/')
async def send_note(time: int = 0):
    with open('data.json', 'r') as file:
        notes = json.load(file)
    return notes["0"]["0"]


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("app:app", reload=True)