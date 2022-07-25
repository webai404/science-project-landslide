from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import urllib.request
import numpy as np
import os.path as path
import os
import cv2 as cv
import argparse
import RPi.GPIO as GPIO
import gmail
import ard
import line

# os.system('./ffmpeg.sh &')
# 設定攝影機
camera = PiCamera()
camera.resolution = (64, 64)
rawCapture = PiRGBArray(camera, size=(64, 64))
# 新視窗命名為Faces
display_window = cv2.namedWindow('Faces')
parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
                                              OpenCV. You can process both videos and images.')
parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.', default='image0.jpg')
parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')
args = parser.parse_args()
if args.algo == 'MOG2':
    backSub = cv.createBackgroundSubtractorMOG2()
else:
    backSub = cv.createBackgroundSubtractorKNN()
camera.framerate = 15
camera.rotation = 180
k = 0
x = 0
water = False
light = False
img_my = False
r = 3

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    k = k + 1
    camera.start_preview()
    img = frame.array
    fgMask = backSub.apply(img)
    fgMask = cv2.medianBlur(fgMask, 3)
    for i in range(63):
        i = i + 1
        for j in range(63):
            j = j + 1
            a = fgMask[1 * i, 1 * j]
            b = fgMask[1 * i - 1, 1 * j]

            c = fgMask[1 * i, 1 * j - 1]
            d = fgMask[1 * i - 1, 1 * j - 1]
            # print(a,',',b,',',c,',',d,',')
            f = a + b + c + d
            # print(f)
            # print(f,i,j)
            if ((f == 252 and k > 3) and (img_my == False)):
                print("img")
                gmail.send(2)
                line.send(2)
                img_my = True
                r += 1
                break

        if (f == 252):
            break
    cv2.imshow('Faces', fgMask)
    cv2.imshow('img', img)
    key = cv2.waitKey(1)

    rawCapture.truncate(0)
    x = ard.check()

    if (x == 1 and not water):
        print("water")
        gmail.send(0)
        line.send(0)
        water = True
        r += 1
    elif (x == 2 and not light):
        print("light")
        light = True
        gmail.send(1)
        line.send(1)
        r += 1
    else:
        print("nope")

    if r == 3:
        break
    if key == ord("q"):  # Press 'q' to quit

        break

    if not ard.check_rain():
        time.sleep(1)
