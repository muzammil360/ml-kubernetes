from utils.download_file import download_if_file_not_exists
from utils.config import model_path

if __name__ == "__main__":
    # filepath = os.path.join("..", "yolov6m.onnx")
    filepath = model_path
    download_if_file_not_exists(
        filepath,
        "https://github.com/meituan/YOLOv6/releases/download/0.2.0/yolov6m.onnx",
    )
