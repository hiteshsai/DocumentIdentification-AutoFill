# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 12:08:47 2019

@author: hitesh.jonnalagadda
"""
import glob
import os
import cv2
test_path = "C:/Users/hitesh.jonnalagadda/Desktop/DL_Project/Synthetic_Cards/MP/"
image_files = glob.glob(os.path.join(test_path, "*"))
a =0
for (i, image_file) in enumerate(image_files):
    im = cv2.imread(image_file)
    im = cv2.resize(im,(500,300))
    cv2.imwrite("C:/Users/hitesh.jonnalagadda/Desktop/DL_Project/Synthetic_Cards/mp_final/DL_%d.jpg" %a,im)
    a+=1