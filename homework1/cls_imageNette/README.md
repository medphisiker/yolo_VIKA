Здесь содержится код для оценки модели `YOLOv8m-cls`

Рассматриваются следующие критерии:
1. число параметров модели;
2. вес файла модели;
3. количество `RAM` потребляемое моделью;
4. время инференса;
5. целевая метрика.

Используется датасет `ImageNette`, предоставляемый `ultralytics`, для решения задачи классификации.

Обучение проведено на 20 эпохах.


Получены следующие результаты:

Таблица `Оценка работы моделей домашнее задание 1`

|            | модель      | задача         | датасет      | число параметров | вес модели | девайс      | RAM            | время инференса                                                                            | целевая метрика                                        |
|------------|-------------|----------------|--------------|------------------|------------|-------------|----------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------|
| Константин | YOLOv8m-cls | классификация  | ImageNette   | 17 053 336       | 65.127MB    | colab   |        418 mb        |   2.0ms preprocess, 15.0ms inference, 0.1ms postprocess per image at shape  (1, 3, 224, 224) | top1_acc: 0.975; top5_acc: 0.998     
согласно `homework_1_cls_imageNette/hw_1.model_metrics.ipynb`