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
from time import localtime


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


# import standard Python libraries for manipulation of files and folders
import glob
import shutil
import os

# import data manipulation libraries
import pandas as pd

### specify location where weather data will be stored
path2weather_data = "D:\\Flights\\Weather data\\"

### for each lnk in the list download the graphs and save to the folder according to date and time of day
if localtime()[3] >= 8 and localtime()[3] < 16:
    folder_time = 'day'
elif localtime()[3] >= 16:
    folder_time = 'evening'
else:
    folder_time = 'night'

folder_name = str(date.today()) + '_' + folder_time
path_to_folder = path2weather_data + folder_name

source_file = "C:\\Users\\pawel\\Downloads\\meteogram_airplus_hd.png"

###############################################################################
# Function checks if the given folder exists and if not creates it
def create_folder(folder_name):
    if path.exists(folder_name) == False:
        os.mkdir(folder_name)
        
###############################################################################
# Function moves a file to a specified folder
def move_file(source_file, target_file):
    # move file with full paths as shutil.move() parameters
    shutil.move(source_file, target_file)

### read in file with locations
locations = pd.read_csv("D://Flights//Weather data//locations.txt")
locations = locations.drop(['Unnamed: 0'], axis = 1)

### if there are new links then add location names to the file and savethe file
new_location = False
for i in range(len(locations)):
    if pd.isna(locations['location_name'][i]):
        locations['location_name'][i] = locations['location_link'][i][53:len(locations['location_link'][i])]
        new_location = True
if new_location == True:
    locations.to_csv("D://Flights//Weather data//locations.txt")


### open webdriver and sign in with my account
driver = webdriver.Chrome("D:\\Flights\\ChromeDrivers\\ChromeDriver0\\chromedriver.exe")
time.sleep(random.randint(5, 10))
driver.get('https://www.meteoblue.com/pl/user/login/index')
time.sleep(random.randint(5, 10))
submit_button = driver.find_elements_by_xpath('//*[@id="accept_all_cookies"]')[0]
submit_button.click()
driver.find_element_by_xpath('//*[@id="username"]').send_keys("XXXX")
time.sleep(random.randint(5, 10))
driver.find_element_by_xpath('//*[@id="password"]').send_keys("XXXX")
time.sleep(random.randint(5, 10))
driver.find_element_by_xpath('//*[@id="wrapper-main"]/div/main/div/div[1]/form[1]/div[4]/input').click()
time.sleep(random.randint(5, 10))

### create folder if it doesn't exist
create_folder(path_to_folder)

for i in range(len(locations)):
    time.sleep(random.randint(5, 10))
    driver.get(locations['location_link'][i])
    time.sleep(random.randint(5, 10))
    element = driver.find_element_by_xpath('//*[@id="chart_download"]/span')
    # download the graph
    actions = ActionChains(driver)
    actions.key_down(Keys.ALT)
    actions.click(element)
    actions.key_up(Keys.ALT)
    actions.perform()
    time.sleep(10)
    
    # move the graph in the specific folder
    target_file = path_to_folder + '\\' + locations['location_name'][i] + '.png'
    move_file(source_file, target_file)

driver.quit()