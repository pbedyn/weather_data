# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 10:28:57 2020

@author: pawel
"""

import os
from os import path
import time

import pandas as pd
import numpy as np
import random
from datetime import date
from datetime import datetime
from time import localtime


# import standard Python libraries for manipulation of files and folders
import glob
import shutil
import os

# import data manipulation libraries
import pandas as pd

# import python image library
from PIL import Image

### specify location where weather data will be stored
test_weather_folder = "D:\\Flights\\Weather test\\"
path2folder = "D:\\Flights\\Weather data\\test\\"

def get_characters(weather_folder):
    
    # create a list of folders within the grid
    subfolders = [f.path for f in os.scandir(weather_folder) if f.is_dir()]
    number = 0
    
    for subfolder in subfolders: 
        allFiles = glob.glob(subfolder + "\\" + "*.png")
        for single_file in allFiles:
            number += 1
            new_file_path = whiten_graph(single_file)
            get_01_digit(new_file_path, number)
            get_02_digit(new_file_path, number)
            get_03_digit(new_file_path, number)
            get_04_digit(new_file_path, number)
            get_05_digit(new_file_path, number)
            get_06_digit(new_file_path, number)
            get_07_digit(new_file_path, number)
            get_08_digit(new_file_path, number)
            get_09_digit(new_file_path, number)
            get_10_digit(new_file_path, number)
            get_11_digit(new_file_path, number)
            get_12_digit(new_file_path, number)
            get_13_digit(new_file_path, number)
            get_14_digit(new_file_path, number)
            get_15_digit(new_file_path, number)
            get_16_digit(new_file_path, number)
            
#            get_m1(new_file_path, number)
#            get_m2(new_file_path, number)
#            get_m3(new_file_path, number)
#            get_m4(new_file_path, number)
#            get_m5(new_file_path, number)
#            get_m6(new_file_path, number)
#            get_m7(new_file_path, number)
#            get_m8(new_file_path, number) 
#            get_m9(new_file_path, number) 
#            get_m10(new_file_path, number)             
#            get_Th1(new_file_path, number)
#            get_Th2(new_file_path, number)
#            get_Th3(new_file_path, number)
#            get_Th4(new_file_path, number) 
            
#            get_slash1(new_file_path, number)
#            get_slash2(new_file_path, number)
#            get_slash3(new_file_path, number)
#            get_top_colon1(new_file_path, number)
#            get_top_colon2(new_file_path, number)
#            get_top_colon3(new_file_path, number)
            
#            get_bottom_colon1(new_file_path, number)
#            get_bottom_colon2(new_file_path, number)
#            get_bottom_colon3(new_file_path, number)
#            get_bottom_colon4(new_file_path, number)
#            get_bottom_colon5(new_file_path, number)
#            get_bottom_colon6(new_file_path, number)
#            get_bottom_colon7(new_file_path, number)
#            get_bottom_colon8(new_file_path, number)
            
#            get_dot1(new_file_path, number)
#            get_dot2(new_file_path, number)
#            get_dot3(new_file_path, number)
#            get_dot4(new_file_path, number)
#            get_dot5(new_file_path, number)
#            get_dot6(new_file_path, number)
            
#            get_hyphen1(new_file_path, number)
#            get_hyphen2(new_file_path, number)
#            get_hyphen3(new_file_path, number)
#            get_hyphen4(new_file_path, number)
#            get_hyphen5(new_file_path, number)
#            get_hyphen6(new_file_path, number)
#            get_hyphen7(new_file_path, number)
#            get_hyphen8(new_file_path, number)
            
            os.remove(new_file_path)
    
def get_01_digit(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (854, 764, 872, 789)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\" + str(number) + "_01.png"
    digit.save(digit_file_path)
    
def get_02_digit(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (854, 792, 872, 817)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\" + str(number) + "_02.png"
    digit.save(digit_file_path)
    
def get_03_digit(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (854, 820, 872, 845)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\" + str(number) + "_03.png"
    digit.save(digit_file_path)
    
def get_04_digit(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (854, 847, 872, 872)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\" + str(number) + "_04.png"
    digit.save(digit_file_path)
    
def get_05_digit(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (874, 764, 892, 789)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\" + str(number) + "_05.png"
    digit.save(digit_file_path)
    
def get_06_digit(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (874, 792, 892, 817)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\" + str(number) + "_06.png"
    digit.save(digit_file_path)

def get_07_digit(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (874, 820, 892, 845)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\" + str(number) + "_07.png"
    digit.save(digit_file_path)

def get_08_digit(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (874, 847, 892, 872)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\" + str(number) + "_08.png"
    digit.save(digit_file_path)
    
def get_09_digit(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (956, 764, 974, 789)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\" + str(number) + "_09.png"
    digit.save(digit_file_path)
    
def get_10_digit(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (956, 792, 974, 817)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\" + str(number) + "_10.png"
    digit.save(digit_file_path)
    
def get_11_digit(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (956, 820, 974, 845)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\" + str(number) + "_11.png"
    digit.save(digit_file_path)
    
def get_12_digit(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (956, 847, 974, 872)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\" + str(number) + "_12.png"
    digit.save(digit_file_path)
    
def get_13_digit(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (987, 764, 1005, 789)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\" + str(number) + "_13.png"
    digit.save(digit_file_path)
    
def get_14_digit(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (987, 792, 1005, 817)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\" + str(number) + "_14.png"
    digit.save(digit_file_path)
    
def get_15_digit(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (1137, 820, 1155, 845)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\" + str(number) + "_15.png"
    digit.save(digit_file_path)

def get_16_digit(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (1109, 847, 1127, 872)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\" + str(number) + "_16.png"
    digit.save(digit_file_path)
    
def get_m1(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (587, 723, 615, 748)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\m1_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_m2(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (711, 723, 739, 748)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\m2_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_m3(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (1489, 723, 1517, 748)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\m3_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_m4(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (1613, 723, 1641, 748)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\m4_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_m5(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (2392, 723, 2420, 748)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\m5_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_m6(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (2516, 723, 2544, 748)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\m6_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_m7(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (641, 723, 669, 748)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\m7_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_m8(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (578, 723, 606, 748)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\m8_" + str(number) + ".png"
    digit.save(digit_file_path)

def get_m9(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (629, 723, 657, 748)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\m9_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_m10(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (2215, 723, 2243, 748)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\m10_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_Th1(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (359, 723, 399, 748)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Th1_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_Th2(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (1261, 723, 1301, 748)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Th2_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_Th3(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (2164, 723, 2204, 748)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Th3_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_Th4(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (961, 723, 1001, 748)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Th4_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_slash1(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (615, 723, 627, 750)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Sl1_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_slash2(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (1518, 723, 1530, 750)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Sl2_" + str(number) + ".png"
    digit.save(digit_file_path)

def get_slash3(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (2420, 723, 2432, 750)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Sl3_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_top_colon1(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (485, 723, 490, 748)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Tc1_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_top_colon2(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (1388, 723, 1393, 748)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Tc2_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_top_colon3(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (2290, 723, 2295, 748)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Tc3_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_bottom_colon1(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (465, 723, 471, 748)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Bc1_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_bottom_colon2(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (465, 792, 471, 817)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Bc2_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_bottom_colon3(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (465, 820, 471, 845)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Bc3_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_bottom_colon4(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (465, 847, 471, 872)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Bc4_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_bottom_colon5(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (1368, 764, 1374, 789)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Bc5_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_bottom_colon6(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (1368, 792, 1374, 817)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Bc6_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_bottom_colon7(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (1368, 820, 1374, 845)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Bc7_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_bottom_colon8(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (1368, 847, 1374, 872)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Bc8_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_dot1(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (527, 792, 532, 817)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Dt1_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_dot2(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (528, 820, 533, 845)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Dt2_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_dot3(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (528, 847, 533, 872)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Dt3_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_dot4(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (1431, 792, 1436, 817)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Dt4_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_dot5(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (1431, 820, 1436, 845)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Dt5_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_dot6(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (1431, 847, 1436, 872)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Dt6_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_hyphen1(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (390, 764, 401, 789)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Hp1_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_hyphen2(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (390, 792, 401, 817)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Hp2_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_hyphen3(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (390, 820, 401, 845)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Hp3_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_hyphen4(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (390, 848, 401, 873)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Hp4_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_hyphen5(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (1293, 764, 1304, 789)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Hp5_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_hyphen6(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (1293, 792, 1304, 817)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Hp6_" + str(number) + ".png"
    digit.save(digit_file_path)
    
def get_hyphen7(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (1293, 820, 1304, 845)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Hp7_" + str(number) + ".png"
    digit.save(digit_file_path)

def get_hyphen8(file_path, number):
    ### read in file with eliminated colours
    img = Image.open(file_path)
    ### crop the first digit
    crop_digit = (1293, 848, 1304, 873)
    digit = img.crop(crop_digit)
    ### save digit as png
    digit_file_path = "D:\\Flights\\Weather data\\Digits\\Hp8_" + str(number) + ".png"
    digit.save(digit_file_path)
    
    
### eliminate colours from the thermal strenght graph
def whiten_graph(file_path):
    img = Image.open(file_path).convert('RGBA')
    px = img.load()

    for x in range(3000):
        for y in range(3600):
            # eliminate the green background
            if px[x, y] == (104, 232, 136, 255):
                img.putpixel([x, y], (248, 248, 248, 255))
            # eliminate the light green background
            if px[x, y] == (216, 240, 168, 255):
                img.putpixel([x, y], (248, 248, 248, 255))
            # eliminate the pink line
            if px[x, y] == (232, 104, 200, 255):
                img.putpixel([x, y], (248, 248, 248, 255))
            # eliminate the red line
            if px[x, y] == (232, 48, 32, 255):
                img.putpixel([x, y], (248, 248, 248, 255)) 
            # eliminate the blue line
            if px[x, y] == (80, 32, 200, 255):
                img.putpixel([x, y], (248, 248, 248, 255))
                
    new_file_path = file_path[0:len(file_path)-4] + "_white.png"
    img.save(new_file_path)
    return new_file_path
    
get_characters(test_weather_folder)


#### Eliminate the same digits - NOT PROPERLY CODED INTO FUNCTION
def eliminate_the_same_digits(digit_file, digit_folder):
    img1 = Image.open(digit_file)
    img1_np = np.array(img1)
    allImages = glob.glob("D:\\Flights\\Weather data\\Digits\\" + str(digit_folder) + "\\*.png")
    for image in allImages:
        img2 = Image.open(image)
        img2_np = np.array(img2)
        mse = np.mean((img2_np - img1_np)**2)
        if mse == 0.0:
            os.remove(image)
        img1.save(digit_file)

digit_folder = "s"
alltemplates = glob.glob("D:\\Flights\\Weather data\\Digits\\" + digit_folder + "\\*.png")
for template in alltemplates:
    eliminate_the_same_digits(template, digit_folder)
        
        
### print maximum distance between the same digits
def print_differences_between_same_digits(digit_folder):
    allImages = glob.glob("D:\\Flights\\Weather data\\Digits\\" + str(digit_folder) + "\\*.png")
    mse_list = []
    for image in allImages:
        img1 = Image.open(image)
        img1_np = np.array(img1)
        for image in allImages:      
            img2 = Image.open(image)
            img2_np = np.array(img2)
            mse_list.append(np.mean((img2_np - img1_np)**2))
    print(digit_folder, max(mse_list))


### print min distance between different digits
def print_differences_between_diff_digits(digit_folder_1, digit_folder_2):
    allImages_1 = glob.glob("D:\\Flights\\Weather data\\Digits\\" + str(digit_folder_1) + "\\*.png")
    allImages_2 = glob.glob("D:\\Flights\\Weather data\\Digits\\" + str(digit_folder_2) + "\\*.png")
    mse_list = []
    for image in allImages_1:
        img1 = Image.open(image)
        img1_np = np.array(img1)
        for image in allImages_2:      
            img2 = Image.open(image)
            img2_np = np.array(img2)
            mse_list.append(np.mean((img2_np - img1_np)**2))
    print(digit_folder_1, digit_folder_2, min(mse_list))


for i in range(10):
    print_differences_between_same_digits(i)
    
for i in range(10):
    print_differences_between_same_digits(i)
    print('xxx')
    for j in range(10):
        print_differences_between_diff_digits(i, j)
    print('yyy')
