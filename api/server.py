# WARNING: following code is needed to workaround a bug which comes while running unit tests
# https://stackoverflow.com/questions/60359157/valueerror-set-wakeup-fd-only-works-in-main-thread-on-windows-on-python-3-8-wit
import sys, asyncio, io

if sys.platform == "win32" and (3, 8, 0) <= sys.version_info < (3, 9, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# ====================
import numpy as np
import cv2

from typing import Union

from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"msg": "Hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/ping")
def get_ping():
    return {"msg": "Pong"}


# TODO: move v1 api into its own folder
# =========== v1 api =============
from .utils.config import model_path
from .services.Yolov6 import Yolov6

model = Yolov6(model_path)


@app.post("/v1/detections")
async def post_detections(file: UploadFile):
    # read the image to get numpy array
    # TODO: understand better
    contents = await file.read()
    np_array = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    # process the image
    processed_image = model.infer(image)

    # Return the processed image as a streaming response
    # TODO: understand better
    _, img_encoded = cv2.imencode(".jpg", processed_image)
    img_bytes = img_encoded.tobytes()

    return StreamingResponse(io.BytesIO(img_bytes), media_type="image/jpeg")
