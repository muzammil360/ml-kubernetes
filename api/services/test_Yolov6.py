import os

import cv2 
from Yolov6 import Yolov6 

model_path = os.path.join('..','yolov6m.onnx')
model = Yolov6(model_path)

def test_yolov6():
    img_path = os.path.join('resources','test_image1.jpg')
    input_image = cv2.imread(img_path)

    output_image = model.infer(input_image)

    assert output_image.shape==input_image.shape