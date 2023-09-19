Здесь содержится код для оценки `YOLOv8l-seg`

1. число параметров модели (46 M)
2. вес файла модели ()
3. количество `RAM` потребляемое моделью
4. время инференса
5. целевая метрика на `val` части датасета

Пример оценки моделей `yolo-seg` не работает с датасетом `MS COCO val 2017` предоставляем `ultralytics`.

Поэтому создадим свой кастомный датасет на сегментацию для исходного `MS COCO val 2017`
Для конвертации исходного датасета из формата MS COCO в формат датасета для сегментации используем репозиторий `JSON2YOLO` ([ссылка](https://github.com/ultralytics/JSON2YOLO)).

Склонируем данный репозтоорий:
```
git clone git@github.com:ultralytics/JSON2YOLO.git
```

Затем перевести датасет в формат `YOLO` используя скрипт `JSON2YOLO/general_json2yolo.py`
Указав на `homework1_segmentation/datasets/ms_coco_val_2017`

Структура итогового датасета для оценки метрик:
```
homework1_segmentation/datasets/ms_coco_val_2017
├──val
|   ├── images
|   └── labels
└── labels.cache
```

Создаем файл `homework1_segmentation/ms_coco_val_2017.yaml`

После этого може оценивать метрики:

```
box map50-95 0.522
box map50 0.688
box map75 0.571

mask map50-95 0.431
mask map50 0.659
mask map75 0.465
```
согласно `homework1_segmentation/YOLOv8_segment.ipynb`
