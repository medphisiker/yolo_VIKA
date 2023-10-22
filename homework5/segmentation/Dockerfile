# образ для контейнера
FROM nvcr.io/nvidia/tensorrt:23.09-py3

# отключаем интерактивные вопросы при установке пакетов
# при создании docker-контейнера
ARG DEBIAN_FRONTEND=noninteractive

# установим opencv-python
# для этого нам понадобится ее зависимость libgl1
# см. https://stackoverflow.com/a/68666500
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python==4.8.1.78

# Установим PyTorch и Cuda
RUN pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 \
    torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118

# Установим ultralytics yolov8
RUN pip install ultralytics==8.0.200

# Зависимости для экспорта yolov8 в ONNX
RUN pip install onnx==1.14.1 onnxsim==0.4.35 install onnxruntime-gpu==1.16.1 \
    openvino-dev>=2023.0 rich==13.6.0 flatbuffers==23.5.26 sympy==1.12 \
    coloredlogs==15.0.1 humanfriendly==10.0 markdown_it_py==2.2.0 \
    mpmath==1.3.0 mdurl==0.1.2

# установим kernel для Jupyter Notebook
RUN pip install ipykernel==6.23.0

# чистим систему от лишнего
RUN apt-get clean && apt-get autoremove

# папка для подключения репозитория с кодом
WORKDIR /workspace