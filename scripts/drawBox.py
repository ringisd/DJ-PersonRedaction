#Import Packages
import cv2
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

filenameStart = "media/Cordinates/"+args.image+'_'+args.start+'_'+args.end+'.csv'
with open(filenameStart) as csv_filestart:
    csvReader = csv.reader(csv_filestart, delimiter=',')
    for row in csvReader:
        frame = row[0]
        #print("Frame Number", frame )
        filename = "media/Input/"+args.image+frame+".png"
        image=cv2.imread(filename)
        image = cv2.rectangle(image, (int(row[1]), int(row[2])), (int(row[3]), int(row[4])), (0,255,0), 5)
        outputfile = "media/Output/"+args.image+frame+".jpg"
        cv2.imwrite(outputfile, image)