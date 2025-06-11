!pip install ultralytics

import cv2
import os
from ultralytics import YOLO

model_path = "model path"
model = YOLO(model_path)
video_path = "video path"

output_dir = "outpyt dir"
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"Failed to open {video_path}")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

output_filename = os.path.basename(video_path).replace(".mp4", "_output.avi")
output_path = os.path.join(output_dir, output_filename)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

print(f"Processing {video_path}, saving to {output_path}")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    results = model(frame)[0]
    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        label = f"{model.names[cls_id]} {conf:.2f}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        font_scale = 0.5 
        thickness = 1
        (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)
        cv2.rectangle(frame, (x1, y1 - 20), (x1 + w, y1), (0, 255, 0), -1)
        cv2.putText(frame, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 0), thickness)

    out.write(frame)
cap.release()
out.release()
print("Video processed and saved!")