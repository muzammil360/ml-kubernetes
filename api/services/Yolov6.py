import cv2

from Yolov6Engine import pre_process, post_process


class Yolov6:
    def __init__(self, model_path):
        self.model_path = model_path
        self.net = cv2.dnn.readNet(self.model_path)

    def infer(self, input_frame):
        detections = pre_process(input_frame.copy(), self.net)
        output_image = post_process(input_frame.copy(), detections)
        return output_image
