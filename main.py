import os
from deta import Deta
from flask import Flask
from fastapi.responses import StreamingResponse

app = Flask(__name__)

app = FastAPI()
deta = Deta(os.getenv("Project_Key")) 
drive = deta.Drive("pics")

'''
@app.route('/', methods=["GET"])
def hello_world():
    return "Hello World"
'''

@app.route('/download/{name}', methods=["GET"])
def download_img():
    res = drive.get(name)"
    return StreamingResponse(res.iter_chunks(1024))
