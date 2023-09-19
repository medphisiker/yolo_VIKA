#homework1

Команда `yolo_VIKA`:
* Владимир Кравцов
* Инесса Фёдорова 
* Константин Щетинников
* Антон Ширяев

Таблица `Оценка работы моделей домашнее задание 1`

|            | модель      | задача         | датасет      | число параметров | вес модели | девайс      | RAM            | время инференса                                                                            | целевая метрика                                        |
|------------|-------------|----------------|--------------|------------------|------------|-------------|----------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------|
| Антон      | YOLOv8l-seg | сегментация    | COCO val2017 | 46.0M            | 88.1mb     | nvidia A10  |                | 0.1ms preprocess, 9.1ms inference, 0.4ms postprocess per images at shape (1, 3, 640, 640)  | mask map50-95 0.431 mask map50 0.659 mask map75 0.465  |
| Инесса     | YOLOv8m-det | детекция       | COCO val2017 | 25.9M            | 52.12mb    | mps         | 98.94 mb       | 1.9ms preprocess, 217.3ms inference, 0.9ms postprocess per image at shape (1, 3, 640, 480) | map0.5 0.521 map0.95 0.371                             |
| Константин | YOLOv8m-cls | классификация  | ImageNette   | 17 053 336       | 65.127MB    | colab   |        418 mb        |   2.0ms preprocess, 15.0ms inference, 0.1ms postprocess per image at shape  (1, 3, 224, 224) | top1_acc: 0.975; top5_acc: 0.998                                                        |
| Вова       | YOLOv8l-cls | классификация  | ImageWoof    | 37.5M            | 72.6Mb     | nvidia A100 | 1548Mb (vram)  | 1.3ms preprocess, 0.3ms inference, 0.0ms postprocess per image at shape (1, 3, 224, 224)   | acc top1 0.925; acc top5 0.995                         |
|            |             |                |              |                  |            |             |                |                                                                                            |                                                