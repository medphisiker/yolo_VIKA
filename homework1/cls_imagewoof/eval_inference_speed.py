from ultralytics import YOLO
from glob import glob

images = glob('/usr/src/datasets/imagewoof/val/**/*.JPEG', 
              recursive=True)
weights_path = '/usr/src/ultralytics/runs/classify/train/weights/last.pt'

model = YOLO(weights_path)
print('start inference...')
result = model(images[:100])

for r in result:
    print(r.speed)

