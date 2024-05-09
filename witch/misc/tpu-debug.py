'''
import tflite_runtime.interpreter as tflite

model = tflite.Interpreter(
    model_path='/home/errc/v/yolov8n_full_integer_quant_edgetpu.tflite',
    experimental_delegates=[tflite.load_delegate('libedgetpu.so.1',{})]
)
'''

from ultralytics import YOLO

# Load a model
model = YOLO('/home/errc/v/yolov8n_full_integer_quant_edgetpu.tflite')  # Load an official model or custom model

# Run Prediction
model.predict('/home/errc/e/ai/test-selfie.jpg', save=True, save_txt=True)