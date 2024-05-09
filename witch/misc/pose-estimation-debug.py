from ultralytics import YOLO
import cv2
from PIL import Image

def test_image(model, img_file):
    img = Image.open(img_file)
    model.predict(source=img, save=True, project='misc/pose-estimation-debug-output')

def test_video(model, video_file):
    cap = cv2.VideoCapture(video_file)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        res = model.track(frame, persist=True, save=True, project='misc/pose-estimation-debug-output')
        annotated_frame = res[0].plot()
        cv2.imshow("yolo tracking test", annotated_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()

if __name__ == "__main__":
    model = YOLO('misc/yolov8s-pose.pt')
    #model.export(format='tflite')
    #tflite_model = YOLO('yolov8s-pose.tflite')
    #test_image(model, 'misc/test-selfie.jpg')
    test_video(model, 'misc/test-selfie.mov')