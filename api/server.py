# WARNING: following code is needed to workaround a bug which comes while running unit tests
# https://stackoverflow.com/questions/60359157/valueerror-set-wakeup-fd-only-works-in-main-thread-on-windows-on-python-3-8-wit 
import sys, asyncio
if sys.platform == "win32" and (3, 8, 0) <= sys.version_info < (3, 9, 0):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# ====================

from typing import Union

from fastapi import FastAPI
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


# =========== v1 api =============

class Detections(BaseModel):
    person: float
    car: float
    dog: float

@app.post("/v1/detections")
def post_detections() -> Detections:
    return Detections(person=0.1,car=0.2,dog=0.3)



