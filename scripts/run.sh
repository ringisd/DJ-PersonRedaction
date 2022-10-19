#!/bin/bash
python3 scripts/Detect.py --image  Barry/img-1300.png --config yolov3.cfg --weights models/yolov3.weights --classes yoloclass.txt
python3 scripts/Detect.py --image  Barry/img-1400.png --config yolov3.cfg --weights models/yolov3.weights --classes yoloclass.txt