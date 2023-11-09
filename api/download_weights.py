import os

from utils.download_file import download_if_file_not_exists

if __name__=='__main__':
    filepath = os.path.join("..", "yolov6m.onnx")
    download_if_file_not_exists(filepath, 'https://github.com/meituan/YOLOv6/releases/download/0.2.0/yolov6m.onnx')