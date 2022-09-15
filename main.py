from deta import Drive
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()
drive = Drive("pics")

# @app.route('/', methods=["GET"])
# def hello_world():
#     return "Hello World"

@app.get("/download/{name}")
def download_img(name: str):
    res = drive.get(name)
    return StreamingResponse(res.iter_chunks(1024), media_type="image/png")
