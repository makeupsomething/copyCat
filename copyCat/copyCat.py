import os
import sys
import cv2
from shutil import copy

def doImageCheck(imgPath, destPath):	
	images = []
	catImages = []
	otherImages = []

	for (dirpath, dirnames, filenames) in os.walk(imgPath):
		images.extend(filenames)
		break

	for i in images:
		filepath = 	imgPath + i
		image = cv2.imread(filepath)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		detector = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")
		rects = detector.detectMultiScale(gray, scaleFactor=1.2,
			minNeighbors=10, minSize=(75, 75))

		if(len(rects) > 0):
			catImages.append(filepath)

	copyImages(catImages, destPath)

def copyImages(images, destPath):
	if(not os.path.isdir(destPath)):
		os.makedirs(destPath)
	for i in images:
		try:
			copy(i, destPath)
		except Exception as ex1:
			print ex1
	#do the copy

def checkImgPath(path):
	if(not path.endswith('/')):
		path += '/'
	return path

imgPath = ''
destPath = ''
args = sys.argv
if(len(args) == 3):
	p = args[1]
	destPath = args[2]
else:
	print 'invalid arguments'
imgPath = checkImgPath(p)
doImageCheck(imgPath, destPath)
