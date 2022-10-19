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

filenameStart = "media/Cordinates/"+args.image+args.start".csv"
filenameEnd = "media/Cordinates/"+args.image+args.start".csv"

#Read Start CSV

#Select Detection