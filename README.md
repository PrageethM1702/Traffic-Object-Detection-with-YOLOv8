# 🚦 Traffic Object Detection with YOLOv8

![Traffic](https://img.shields.io/badge/YOLOv8-Traffic%20Detection-green?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![License](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)

This project implements a YOLOv8-based object detection model trained on a public traffic dataset to detect multiple classes including bicycles, buses, cars, motorbikes, and persons in urban environments.

## 📁 Dataset

- Source: [Kaggle - Traffic Detection Project](https://www.kaggle.com/datasets/yusufberksardoan/traffic-detection-project)
- License: CC BY 4.0
- Classes: `bicycle`, `bus`, `car`, `motorbike`, `person`

## 🧠 Model

- YOLOv8 nano (yolov8n.pt)
- Trained for 100 epochs
- Image size: 640x640
- Batch size: 16

## 🔍 Objectives

- Detect and classify traffic objects in real-time
- Evaluate object detection performance using precision-recall metrics
- Enable future deployment to embedded systems for smart traffic surveillance

## 📊 Features

- Cleaned and validated YOLO-format dataset
- Data analysis: class distribution, label completeness
- Model performance visualized via PR/F1/P/R curves and confusion matrix

## 📌 Notes

- Dataset analysis and model training done using Python 3.10
- All training conducted on Kaggle notebooks using Ultralytics YOLOv8
- Visual outputs include detection batches and evaluation plots

## ✅ Future Improvements

- Hyperparameter tuning for better accuracy
- Deployment on edge devices
- Integration with real-time video streams

## 🙏 Acknowledgements

- [Yusuf Berk Sardoğan](https://www.kaggle.com/datasets/yusufberksardoan) for dataset creation
- [Ultralytics](https://github.com/ultralytics/ultralytics) for YOLOv8 framework
- [Roboflow](https://universe.roboflow.com/) for dataset formatting and augmentation tools
