from ultralytics import YOLO

# Load a model
model = YOLO('yolov8l-cls.pt')  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data='imagewoof', epochs=20, imgsz=224, batch=32)