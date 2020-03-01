# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 10:28:57 2020

@author: pawel
"""

### system packages for manipulation of files and folders
import os
from os import path
import shutil
import time
import re
from datetime import date
import datetime
from time import localtime

### data manipulation packages
import pandas as pd
import random

### webscraping packages
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

###############################################################################
### Funtion reads MB user name and password information from a file
def get_uname_pwd(path_to_uname_pwd_file):
    uname_pwd_df = pd.read_csv(path_to_uname_pwd_file)
    uname_pwd_df = uname_pwd_df.drop(['Unnamed: 0'], axis = 1) 
    u_name = uname_pwd_df['user_name'][0]
    password = uname_pwd_df['password'][0]
    return u_name, password

###############################################################################
# Function checks folder for the given scrape exists and if not creates it
def create_folder(path_to_weather_data):
    ### determine extension of the folder based on time of day
    if localtime()[3] == 8:
        folder_time = 'day'
    elif localtime()[3] == 20:
        folder_time = 'evening'
    else:
        folder_time = 'test'
    ### folder name is today's date plus extension based on time of day
    folder_name = str(date.today()) + '_' + folder_time
    path_to_folder = path_to_weather_data + folder_name
    ### create folder if it doesn't exist        
    if path.exists(path_to_folder) == False:        
        os.mkdir(path_to_folder)
    return path_to_folder
        
###############################################################################
# Function moves the downloaded file to a specified location
def move_file(source_file, target_file):
    # move file with full paths as shutil.move() parameters
    shutil.move(source_file, target_file)

###############################################################################
### Function returning hour and minute of latest update of the weather forecast    
def scrape_MB_update():
    source = requests.get('https://www.meteoblue.com/en/weather/week/sura%c5%bc_poland_757751').text
    soup = BeautifulSoup(source, 'lxml')
    last_update = soup.find_all('span', class_= 'value')[3]
    last_update = str(last_update)
    ###  length of update appears to change depending on the time
    try:    
        last_update_hour = int(last_update[32:34])
    except:
        last_update_hour = int(last_update[31:33])    
    try:
        last_update_minute = int(last_update[35:37])
    except:
        last_update_minute = int(last_update[34:36])
    return last_update_hour, last_update_minute

###############################################################################
### Function to scrape air charts pdf files and save to folder
def scrape_MB_aircharts(locations, path_to_folder, path_to_chrome):      
    ### open webdriver and sign in with my account
    driver = webdriver.Chrome(path_to_chrome)
    time.sleep(random.randint(5, 10))
    driver.get('https://www.meteoblue.com/pl/user/login/index')
    time.sleep(random.randint(5, 10))
    submit_button = driver.find_elements_by_xpath('//*[@id="accept_all_cookies"]')[0]
    submit_button.click()
    ### get user name and password information from the credentials file
    u_name, password = get_uname_pwd(path_to_uname_pwd_file)
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(u_name)
    time.sleep(random.randint(5, 10))
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    time.sleep(random.randint(5, 10))
    driver.find_element_by_xpath('//*[@id="wrapper-main"]/div/main/div/div[1]/form[1]/div[4]/input').click()
    time.sleep(random.randint(5, 10))
    
    ### scrape locations based on the list
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
        # simple error management (if file doesn't exist wait a little longer)
        try:
            move_file(source_file, target_file)
        except:
            time.sleep(random.randint(5, 10))
            move_file(source_file, target_file)
    driver.quit()

###############################################################################
### Function to scrape data on temperature, wind, gust and cloud cover  
def scrape_MB_data(locations, path_to_folder, path2chrome):
    # open chrome, go to 7day weather and accept cookies
    driver = webdriver.Chrome(path2chrome)
    driver.get("https://www.meteoblue.com/pl/pogoda/tydzie%C5%84/osiek_polska_763011?day=2")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="accept_all_cookies"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="tab_wrapper"]/div[4]/div/div[2]/div/span[1]').click()
    time.sleep(3)
    
    # Loop over locations in the locations table
    for loc in range(len(locations)):
        frame = pd.DataFrame()
        list_date = []
        list_hour = []
        list_wind_direction = []
        list_speed = []
        list_gust = []
        list_cloud = []
        list_temperature = []
        today = datetime.date.today()
                
        for day_no in range(1, 8):    
            day_to_url = locations['location_7day_link'][loc] + "?day=" + str(day_no)
            driver.get(day_to_url)
            time.sleep(2)
            html = driver.page_source
            
            file_name = locations["location_name"][loc] + ".csv"
            file_name = path_to_folder + '\\' + file_name
            day_to_frame = today + datetime.timedelta(days = day_no - 1)
    
            # make a framework with empty columns
            num_to_xpath = str(day_no * 2)
            for xhour in range(1, 25):
                # scrape wind speed
                xpath = '//*[@id="tab_wrapper"]/div[' + num_to_xpath + ']/div/div[3]/div/table/tbody/tr[6]/td[' + str(xhour) + ']'
                speed = driver.find_element(By.XPATH, xpath).text
                speedms = float(speed)/3.6
                speedms = round(speedms, 1)
                list_date.append(day_to_frame)
                list_speed.append(speedms)
                list_hour.append(xhour)
                # scrape wind gusts
                xhour = str(xhour)
                xpath = '//*[@id="tab_wrapper"]/div[' + num_to_xpath + ']/div/div[3]/div/table/tbody/tr[7]/td[' + xhour + ']'
                gust = driver.find_element(By.XPATH, xpath).text
                gustms = float(gust)/3.6
                gustms = round(gustms, 1)
                list_gust.append(gustms)
                # scrape temperature
                xpath = '//*[@id="tab_wrapper"]/div[' + num_to_xpath + ']/div/div[3]/div/table/tbody/tr[4]/td[' + str(xhour) + ']'
                temp = driver.find_element(By.XPATH, xpath).text
                list_temperature.append(temp)
        
            # scrape cloud icon
            # take source of webpage and find picons
            soup = BeautifulSoup(html, 'lxml')
            soup_picon = soup.find_all(class_=re.compile('picon'))
    
            for i, element in enumerate(soup_picon):
                if i >= 8 and i <= 31:
                    element = str(element)
                    # make it clear
                    glyphnumber = element
                    glyphnumber = glyphnumber.replace('<div class="picon ', "")
                    glyphnumber = glyphnumber.replace('_night" title="', " ")
                    glyphnumber = glyphnumber.replace('_day" title="', " ")
                    glyphnumber = glyphnumber.replace('"></div>', "")
                    # separate pictogram name and description
                    pi = glyphnumber[0:3]
                    descr = glyphnumber[3:]
                    pi_and_descr = pi + "," + descr
                    list_cloud.append(pi_and_descr)
    
            # scrape wind direction
            # take webpage source and find wind glyphs
            soup_glyph = soup.find_all(class_=re.compile('glyph winddir'))
            # make some clear
            for i, element in enumerate(soup_glyph):
                if i >= 11 + day_no - 1 and i <= 34 + day_no - 1:
                    element = str(element)
                    element = element.replace('<span class="glyph winddir ', '')
                    element = element.replace('"></span>', "")
                    list_wind_direction.append(element)
    
        frame["date"] = list_date
        frame["hour"] = list_hour
        frame["dir"] = list_wind_direction
        frame["speed, m/s"] = list_speed
        frame["gust, m/s"] = list_gust
        frame["temp"] = list_temperature
        frame["cloud"] = list_cloud
        frame.to_csv(file_name)
        time.sleep(5)
    driver.quit()
    
###############################################################################
### Infinite loop - needs a rethink but works so far
### Check current time and if it's 8 or 20 start checking for updates
def inf_loop(locations, path_to_weather_data, path_to_chrome0, path_to_chrome1):  
    ### infinite loop waiting for the time to change to scrape new graphs      
    while localtime()[3] < 25:
        ### updates are done twice per day at approx. 08:22 and approx. 20:30
        if localtime()[3] == 8:
            current_hour = localtime()[3]
            current_minute = localtime()[4]
            print(localtime()[3], ':', localtime()[4], "checking ...")
            ### check for an update
            last_update_hour, last_update_minute = scrape_MB_update()
            ### if update made and it's 10 minutes past the update (just in case)
            ### then commence scraping
            if last_update_hour == current_hour and current_minute > last_update_minute + 10:
                path_to_folder = create_folder(path_to_weather_data)
                print(localtime()[3], ':', localtime()[4], "scraping ...")
                scrape_MB_aircharts(locations, path_to_folder, path_to_chrome0)
                scrape_MB_data(locations, path_to_folder, path_to_chrome1)
                print(localtime()[3], ':', localtime()[4], "sleeping ...")
                time.sleep(3600)
            time.sleep(300)
        if localtime()[3] == 20:
            current_hour = localtime()[3]
            current_minute = localtime()[4]
            print(localtime()[3], ':', localtime()[4], "checking ...")
            ### check for an update
            last_update_hour, last_update_minute = scrape_MB_update()
            ### if update made and it's 10 minutes past the update (just in case)
            ### then commence scraping
            if last_update_hour == current_hour and current_minute > last_update_minute + 10:
                path_to_folder = create_folder(path_to_weather_data)
                print(localtime()[3], ':', localtime()[4], "scraping ...")
                scrape_MB_aircharts(locations, path_to_folder, path_to_chrome0)
                scrape_MB_data(locations, path_to_folder, path_to_chrome1)
                print(localtime()[3], ':', localtime()[4], "sleeping ...")
                time.sleep(3600)
            time.sleep(300)
        else:
            print(localtime()[3], ':', localtime()[4], "waiting ...")
            time.sleep(300)

###############################################################################
### Main
if __name__ == "__main__":
    
    ### specify location where weather data will be stored
    path_to_weather_data = "D:\\Flights\\Weather data\\"
    ### location of the user name and password file
    path_to_uname_pwd_file = "D:\\Flights\\Weather data\\MB_haslo.txt"
    ### source_file is where MB will download the pdf file
    source_file = "C:\\Users\\pawel\\Downloads\\meteogram_airplus_hd.png"

    ### read in file with locations
    locations = pd.read_csv("D:\\Flights\\Weather data\\locations.txt")
    locations = locations.drop(['Unnamed: 0'], axis = 1)
    
    ### path to chrome drivers
    path_to_chrome0 = "D:\\Flights\\ChromeDrivers\\Chromedriver0\\chromedriver.exe"
    path_to_chrome1 = "D:\\Flights\\ChromeDrivers\\Chromedriver1\\chromedriver.exe"
    
    # initiate the infinite loop
    inf_loop(locations, path_to_weather_data, path_to_chrome0, path_to_chrome1)