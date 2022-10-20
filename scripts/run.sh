#!/bin/bash

SEQ=$1
S=$2
E=$3


python3 scripts/Detect.py --image  ${SEQ}${S} --config yolov3.cfg --weights models/yolov3.weights --classes yoloclass.txt
python3 scripts/Detect.py --image  ${SEQ}${E} --config yolov3.cfg --weights models/yolov3.weights --classes yoloclass.txt
python3 scripts/GenerateCords.py --image  ${SEQ} --start ${S} --end ${E}
python3 scripts/drawBox.py --image  ${SEQ} --start ${S} --end ${E}
