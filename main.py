import cv2
from ultralytics import YOLO
import yaml


with open("config/yolov8.yml", "r") as file:
    constants = yaml.safe_load(file)


class Detector:
    def __init__(self) -> None:
        model = YOLO(constants["model_path"])
        self.det_results = model(
            constants["video_path"],
            stream=True,
            classes=constants["person_class"],
            conf=constants["confidence_score"],
        )
        width, height, fps = 1920, 1080, 10
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self.out = cv2.VideoWriter(constants["out_video"], fourcc, fps, (width, height))

    def detect_person(self):
        for result in self.det_results:
            xywh_bb = result.boxes.xywh
            annotated_img = result.plot()
            print(annotated_img.shape)
            self.out.write(annotated_img)
        self.out.release()


if __name__ == "__main__":
    model = Detector()
    model.detect_person()
