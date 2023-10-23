# Описание

Это ДЗ выполнялась в `miniconda`. 

Создание виртуального окружения из файла `homework5/segmentation/environment.yml` не работает корректно!

Поскольку оно восстанавливается не в той же последовательности установки.

# Последовательность установки пакетов

Проще всего воспроизвести рабочее окружение создав новое виртуально окружение и последовательно выполнить в нем команды:
```
pip install ultralytics
pip install ipykernel
pip install onnx>=1.12.0  onnxsim>=0.4.1
pip install onnxruntime-gpu
pip install onnxruntime
pip install nvidia-tensorrt
pip install openvino-dev>=2023.0
```