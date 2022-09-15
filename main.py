from deta import Drive
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()
drive = Drive("pics")

@app.get("/{name}")
def download_img(name: str):
    res = drive.get(name)
    return StreamingResponse(res.iter_chunks(1024))
