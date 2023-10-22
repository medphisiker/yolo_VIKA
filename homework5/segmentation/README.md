# Описание

Это ДЗ выполнялась в `miniconda`. 

Виртуальное окружение сохранено в файле `homework5/segmentation/environment.yml`.

Создаем новое виртуальное окружение:
```
conda env create -f environment.yml
```

активируем его
```
conda activate hw5
```

Работаем в нем =)

# docker image pytorch_yolov8 c поддержкой nVidia GPU

Docker-образ, содержащий рабочее окружение для запуска `ultralytics yolov8`.

Данный репозиторий был подготовлен для доклада `Используем GPU nvidia внутри docker-контейнера`([ссылка на видеозапись](https://youtu.be/NyAXipOWz48)) для участников онлайн курса `MLOps и production подход к ML исследованиям 2.0` ([ссылка на курс](https://ods.ai/tracks/ml-in-production-spring-23)).
![Первая страница презентации доклада](repo_pics/Первая_страница_презентации_доклада.jpg)

Файл презентации доклада размещен в данном репозитории `./Презентация.pdf`.

Так же была подготовлена  статья на `Medium` ([сслыка](https://medium.com/@med.phisiker/используем-gpu-nvidia-внутри-docker-контейнера-e6aa73c40442)).

# Сборка docker-образа

* открываем терминал
* клонируем репозиторий с помощью git clone
* переходим в каталог `.devcontainer`, выполнив команду:
```
 cd .devcontainer
```

* выполняем команду сборки:

```
docker build -t pytorch_yolov8:0.0.1 .
```

# Запуск docker-контейнера

Перейдем в каталог репозитория, выполнив команду:
```
cd ..
```

Выполним запуск контейнера следующей командой:
```
docker run \
    --gpus all \
    --rm \
    -it \
    -v ./homework5/segmentation:/workspace \
    pytorch_yolov8:0.0.1
```

`Docker-образ` содержит рабочее окружение (все необходимые зависмости) для запуска `ultralytics yolov8` - `python`-скриптов, `Jupyter Notebook'ов` и нейронных сетей семейства `YOLOv8`.
Но самих скриптов и файлов нейронных сетей в нем нет.

Поэтому при запуске контейнера, к нему нужно примонтировать папку `./yolov8` с кодом.

# Последовательность установки пакетов

pip install ultralytics
pip install ipykernel
pip install onnx>=1.12.0  onnxsim>=0.4.1
pip install onnxruntime-gpu
pip install onnxruntime
pip install nvidia-tensorrt
pip install openvino-dev>=2023.0