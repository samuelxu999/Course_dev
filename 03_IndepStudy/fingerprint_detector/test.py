## Reference: https://medium.com/spidernitt/an-implementation-of-fingerprint-detection-with-python-f143d20c3a96

import cv2
import numpy as np
import os

def detect_fingerprint():
    ## -------------- load the test file ----------------
    fingerprint_test = cv2.imread("fp1.tif")

    for file in [file for file in os.listdir("database")]:
        ## ------------- Matching with the database -------------------
        fingerprint_database_image = cv2.imread("./database/"+file)
        sift = cv2.xfeatures2d.SIFT_create()
        keypoints_1, descriptors_1 = sift.detectAndCompute(fingerprint_test, None)
        keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_database_image, None)

        matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10), dict()).knnMatch(descriptors_1, descriptors_2, k=2)
        match_points = []

        for p, q in matches:
          if p.distance < 0.1*q.distance:
             match_points.append(p)

        ## ------------ Detecting the fingerprint matched ID -------------------
        keypoints = 0

        if len(keypoints_1) <= len(keypoints_2):
          keypoints = len(keypoints_1)            
        else:
          keypoints = len(keypoints_2)

        if (len(match_points) / keypoints)>0.95:
          print("% match: ", len(match_points) / keypoints * 100)
          print("Figerprint ID: " + str(file)) 


if __name__ == '__main__':
    detect_fingerprint()
