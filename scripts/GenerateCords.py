import argparse
import csv


ap = argparse.ArgumentParser()
ap.add_argument('-i','--image', required=True,
                help = 'Path to input image')
ap.add_argument('-s','--start', required=True,
                help = 'Start Frame Number')
ap.add_argument('-e','--end', required=True,
                help = 'End Frame Number')
args = ap.parse_args()

filenameStart = "media/Cordinates/"+args.image+args.start+".csv"
filenameEnd = "media/Cordinates/"+args.image+args.end+".csv"


#Read Start CSV
with open(filenameStart) as csv_filestart:
    csvReader = csv.reader(csv_filestart, delimiter=',')
    rowStart = list(csvReader)
    print("Start Frame Detections")
    print(rowStart)

#Select Detection
leftStart = 0 
topStart = 0
rightStart = 0
bottomStart = 0

det = input("Select Detection")
print(rowStart[int(det)-1])
target = rowStart[int(det)-1]
leftStart = int(target[0])
topStart = int(target[1])
rightStart = int(target[2])
bottomStart = int(target[3])

#Repeat for End
#Read End CSV
with open(filenameEnd) as csv_fileend:
    csvReaders = csv.reader(csv_fileend, delimiter=',')
    rowEnd = list(csvReaders)
    print("End Frame Detections")
    print(rowEnd)

#Select Detection
leftEnd = 0 
topEnd = 0
rightEnd = 0
bottomEnd = 0

det = input("Select Detection")
print(rowEnd[int(det)-1])
target = rowEnd[int(det)-1]
leftEnd = int(target[0])
topEnd = int(target[1])
rightEnd = int(target[2])
bottomEnd = int(target[3])

#Calculate in between frames

#Frames Between
length = int(args.end)-int(args.start)
print("Number of Frames is", length)

#Calculate the movement between each frame

leftIter = (leftEnd - leftStart) / length
topIter = (topEnd - topStart) / length
rightIter = (rightEnd - rightStart) / length
bottomIter = (bottomEnd - bottomStart) / length

fileName = "media/Cordinates/"+args.image+'_'+args.start+'_'+args.end+'.csv'
f = open(fileName, 'a')
writer = csv.writer(f)
for i in range (0, length):
    L = round(leftStart + (leftIter * i))
    T = round(topStart + (topIter * i))
    R = round(rightStart + (rightIter * i))
    B = round(bottomStart + (bottomIter * i))
    F = int(args.start) + i
    writer.writerow([F,L,T,R,B])
f.close()
