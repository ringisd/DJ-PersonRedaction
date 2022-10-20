#Import Packages
import cv2
import argparse
import csv
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image', required=True,
                help = 'Path to input image')
ap.add_argument('-s','--start', required=True,
                help = 'Start Frame Number')
ap.add_argument('-e','--end', required=True,
                help = 'End Frame Number')
args = ap.parse_args()


#Pixelate ROI
def anonymize_pixelate(image, blocks=3):
	# divide the input image into NxN blocks
	(h, w) = image.shape[:2]
	xSteps = np.linspace(0, w, blocks + 1, dtype="int")
	ySteps = np.linspace(0, h, blocks + 1, dtype="int")
	# loop over the blocks in both the x and y direction
	for i in range(1, len(ySteps)):
		for j in range(1, len(xSteps)):
			# compute the starting and ending (x, y)-coordinates
			# for the current block
			startX = xSteps[j - 1]
			startY = ySteps[i - 1]
			endX = xSteps[j]
			endY = ySteps[i]
			# extract the ROI using NumPy array slicing, compute the
			# mean of the ROI, and then draw a rectangle with the
			# mean RGB values over the ROI in the original image
			roi = image[startY:endY, startX:endX]
			(B, G, R) = [int(x) for x in cv2.mean(roi)[:3]]
			cv2.rectangle(image, (startX, startY), (endX, endY),
				(B, G, R), -1)
	# return the pixelated blurred image
	return image

# Open Co-ordinate file
filenameStart = "media/Cordinates/"+args.image+'_'+args.start+'_'+args.end+'.csv'
with open(filenameStart) as csv_filestart:
    csvReader = csv.reader(csv_filestart, delimiter=',')
    for row in csvReader:
        frame = row[0]
        #print("Frame Number", frame )
        filename = "media/Input/"+args.image+frame+".png"
        image=cv2.imread(filename)
        #Draw Box
        image = cv2.rectangle(image, (int(row[1]), int(row[2])), (int(row[3]), int(row[4])), (0,255,0), 5)
        person = image[int(row[2]):int(row[4]), int(row[1]):int(row[3])]
        anonymize_pixelate(person, blocks=3)
        image[int(row[2]):int(row[4]), int(row[1]):int(row[3])] = person
        outputfile = "media/Output/"+args.image+frame+".jpg"
        cv2.imwrite(outputfile, image)


