#!/usr/bin/env python3
import os
import stat 
import argparse
import csv

ap = argparse.ArgumentParser()
ap.add_argument('-n','--name', required=True,
                help = 'FileName') # CSV and Video should have same name
args = ap.parse_args()
print(args.name)
rowNum = 0
command = "ffmpeg -i "+args.name+".mp4 -filter_complex \\ \n \" "
# Read CSV for coordinates
csvFilename = args.name+".csv"
with open(csvFilename, newline='') as csvFile:
    cordReader = csv.reader(csvFile, delimiter=',')
    for row in cordReader:
        frame = row[0]
        left = row[1]
        top = row[2]
        right = row[3]
        bottom = row[4]
        width = int(right) - int(left)
        height = int(bottom) - int(top)
        w = str(width)
        h = str(height)
        nframe = int(frame) + 1
        nexFrame = str(nframe)
        # Generate the worst ffmpeg command ever
        command = command + "[0:v]crop="+w+":"+h+":"+left+":"+top+",boxblur=10:enable='between(n,"+frame+","+nexFrame+")\'[fg]; \\ \n [0:v][fg]overlay="+left+":"+top+"[v]; \\ \n"
        rowNum = rowNum + 1
command = command + "[0:v]null[v]\" -map \"[v]\" -c:v libx264  "+args.name+"_redact.mp4"
print(command)

    

# Create Bash Script

# Run Bash Script