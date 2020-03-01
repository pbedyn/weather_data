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

import pytesseract

### specify location where weather data will be stored
path_to_test_folder = "D:\\Flights\\Weather test\\"

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

### This function determines number of regions of interest and their starting points  
def get_Th(file_path):
    region_of_interest_start = []
    Th_template = []
    ### read in the Th images
    ThImages = glob.glob("D:\\Flights\\Weather data\\Characters\\t\\*.png")
    for image in ThImages:
        Th_template.append(np.array(Image.open(image)))

    ### initiate coordinates of the last m found
    last_crop_digit = (200, 700, 228, 725)    
        
    ### read in the graph
    img = Image.open(file_path).convert('RGBA')
    for y in range(700, 800):
        for x in range(200, 2900):
            crop_digit = (x, y, x + 40, y + 25)
            digit = img.crop(crop_digit)        
            for i in range(len(Th_template)):          
                mse = np.mean((digit - Th_template[i])**2)
                if mse < 3:
                    ### if new m found differs significantly in location from the last one
                    if crop_digit[0] - last_crop_digit[0] > 5:
                        region_of_interest_start.append(x)
                        #digit_file_path = "D:\\Flights\\Weather data\\Digits\\" + str(y) + "_" + str(x) + ".png"
                        #digit.save(digit_file_path)
                        last_crop_digit = crop_digit
    region_of_interest_start = list(dict.fromkeys(region_of_interest_start))
    return region_of_interest_start           

### This function determines end points of the regions of interest                    
def get_m(file_path):
    region_of_interest_end = []
    m_template = []
    ### read in the Th images
    mImages = glob.glob("D:\\Flights\\Weather data\\Characters\\m\\*.png")
    for image in mImages:
        m_template.append(np.array(Image.open(image))) 
    
    ### initiate coordinates of the last m found
    last_crop_digit = (200, 700, 228, 725)    
    ### read in the graph
    img = Image.open(file_path).convert('RGBA')
    for y in range(700, 800):
        for x in range(200, 2900):
            crop_digit = (x, y, x + 28, y + 25)
            digit = img.crop(crop_digit)        
            for i in range(len(m_template)):          
                mse = np.mean((digit - m_template[i])**2)
                if mse < 1:
                    ### if new m found differs significantly in location from the last one
                    if crop_digit[0] - last_crop_digit[0] > 5:
                        region_of_interest_end.append(x)
                        last_crop_digit = crop_digit
    region_of_interest_end = list(dict.fromkeys(region_of_interest_end))
    return region_of_interest_end

### clears section of the image where digit was identified
def clear_section(image, x, y):
    for i in range(x, x + 24):
        for j in range(y, y + 18):
            image.putpixel([i, j], (248, 248, 248, 255))
    return image
    

digit_threshold = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
### read in the digits
digits_folder = "D:\\Flights\\Weather data\\Digits"
subfolders = [f.path for f in os.scandir(digits_folder) if f.is_dir()]
digits_template = []
digits = []
digits_thresholds = []
for subfolder in subfolders:
    allImages = glob.glob(subfolder + "\\" + "*.png")
    for image in allImages:
        digits_template.append(np.array(Image.open(image)))
        digit_from_subfolder = int(subfolder[len(subfolder) - 1:len(subfolder)])
        digits.append(digit_from_subfolder)
        digits_thresholds.append(digit_threshold[digit_from_subfolder])
        
char_threshold = [1, 1, 1, 1, 1, 1]
char_x = [6, 5, 11, 28, 12, 40]
char_y = [25, 25, 25, 25, 27, 25]
### read in the digits
chars_folder = "D:\\Flights\\Weather data\\Characters"
subfolders = [f.path for f in os.scandir(chars_folder) if f.is_dir()]
chars_template = []
chars = []
chars_x = []
chars_y = []
chars_thresholds = []
for subfolder in subfolders:
    allImages = glob.glob(subfolder + "\\" + "*.png")
    for image in allImages:
        chars_template.append(np.array(Image.open(image)))
        char_from_subfolder = subfolder[len(subfolder) - 1:len(subfolder)]
        chars.append(char_from_subfolder)
        if char_from_subfolder == 'c':
            chars_thresholds.append(char_threshold[0])
            chars_x.append(char_x[0])
            chars_y.append(char_y[0])
        if char_from_subfolder == 'd':
            chars_thresholds.append(char_threshold[1])
            chars_x.append(char_x[1])
            chars_y.append(char_y[1])
        if char_from_subfolder == 'h':
            chars_thresholds.append(char_threshold[2])
            chars_x.append(char_x[2])
            chars_y.append(char_y[2])
        if char_from_subfolder == 'm':
            chars_thresholds.append(char_threshold[3])
            chars_x.append(char_x[3])
            chars_y.append(char_y[3])
        if char_from_subfolder == 's':
            chars_thresholds.append(char_threshold[4])
            chars_x.append(char_x[4])
            chars_y.append(char_y[4])
        if char_from_subfolder == 't':
            chars_thresholds.append(char_threshold[5])
            chars_x.append(char_x[5])
            chars_y.append(char_y[5])
            
### eliminate colours from the thermal strenght graph
def get_digits(file_path, digits_template, digits_thresholds, digits, start, end):
    
    digits_found = []
    ### read in the graph
    img = Image.open(file_path).convert('RGBA')
    for y in range(700, 900):
        for x in range(start, end):
            # eliminate the green background
            crop_digit = (x, y, x + 18, y + 25)
            digit = img.crop(crop_digit)        
            for i in range(len(digits_template)):          
                mse = np.mean((digit - digits_template[i])**2)
                if mse < digits_thresholds[i]:
#                    digit_file_path = "D:\\Flights\\Weather data\\Digits\\" + str(y) + "_" + str(x) + ".png"
#                    digit.save(digit_file_path)                    
#                    print(digits[i], mse)
                    digits_found.append(digits[i])
                    #img = clear_section(img, x, y)
    return digits_found

### eliminate colours from the thermal strenght graph
def get_characters(file_path, chars_template, chars_thresholds, chars, chars_x, chars_y, start, end):
    
    chars_found = []
    ### read in the graph
    img = Image.open(file_path).convert('RGBA')
    for y in range(700, 900):
        for x in range(start, end):
            for i in range(len(chars_template)):
                # eliminate the green background
                crop_char = (x, y, x + chars_x[i], y + chars_y[i])
                my_char = img.crop(crop_char) 
                mse = np.mean((my_char - chars_template[i])**2)
                if mse < chars_thresholds[i]:
#                    my_char_file_path = "D:\\Flights\\Weather data\\Characters\\" + str(y) + "_" + str(x) + ".png"
#                    my_char.save(my_char_file_path)                    
                    chars_found.append(chars[i])
                    #img = clear_section(img, x, y)
    return chars_found
                       

def get_regions_of_interest(graphs_folder):
    # create a list of folders within the grid
    subfolders = [f.path for f in os.scandir(graphs_folder) if f.is_dir()]

    for subfolder in subfolders: 
        allFiles = glob.glob(subfolder + "\\" + "*.png")
        for single_file in allFiles:
            print(single_file)
            new_file_path = whiten_graph(single_file)
            region_of_interest_start = get_Th(new_file_path)
            region_of_interest_end = get_m(new_file_path)
            if len(region_of_interest_start) == 3:
                n_region_of_interest = 3
            if len(region_of_interest_start) == 2 and len(region_of_interest_end) > 4:
                n_region_of_interest = 3
            if len(region_of_interest_start) == 2 and len(region_of_interest_end) <= 4:
                n_region_of_interest = 2
            if len(region_of_interest_start) == 1 and len(region_of_interest_end) <= 4:
                n_region_of_interest = 2

            region_of_interest = []
            # standard case of 3 * Th and 6 * m
            if len(region_of_interest_start) == 3 and len(region_of_interest_end) == 6:
                region_of_interest.append(region_of_interest_start[0])
                region_of_interest.append(region_of_interest_end[1] + 32)
                region_of_interest.append(region_of_interest_start[1])
                region_of_interest.append(region_of_interest_end[3] + 32)
                region_of_interest.append(region_of_interest_start[2])
                region_of_interest.append(region_of_interest_end[5] + 32)
                
            # pathological case of 3 * Th and less than 6 * m
            if len(region_of_interest_start) == 3 and len(region_of_interest_end) < 6:
                region_of_interest.append(region_of_interest_start[0])
                region_of_interest.append(region_of_interest_start[0] + 382)
                region_of_interest.append(region_of_interest_start[1])
                region_of_interest.append(region_of_interest_start[1] + 382)
                region_of_interest.append(region_of_interest_start[2])
                region_of_interest.append(region_of_interest_start[2] + 382)

            # pathological case of less than 3 * Th and 6 * m
            if len(region_of_interest_start) < 3 and len(region_of_interest_end) == 6:
                region_of_interest.append(region_of_interest_end[1] - 350)
                region_of_interest.append(region_of_interest_end[1])
                region_of_interest.append(region_of_interest_end[3] - 350)
                region_of_interest.append(region_of_interest_end[3])
                region_of_interest.append(region_of_interest_end[5] - 350)
                region_of_interest.append(region_of_interest_end[5]) 
                
            # standard case of 2 * Th and 4 * m
            if len(region_of_interest_start) == 2 and len(region_of_interest_end) == 4:
                region_of_interest.append(region_of_interest_start[0])
                region_of_interest.append(region_of_interest_end[1] + 32)
                region_of_interest.append(region_of_interest_start[1])
                region_of_interest.append(region_of_interest_end[3] + 32)
            
            # standard case of 2 * Th and less than 4 * m
            if len(region_of_interest_start) == 2 and len(region_of_interest_end) < 4:
                region_of_interest.append(region_of_interest_start[0])
                region_of_interest.append(region_of_interest_start[0] + 382)
                region_of_interest.append(region_of_interest_start[1])
                region_of_interest.append(region_of_interest_start[1] + 382)

            # pathological case of less than 2 * Th and 4 * m
            if len(region_of_interest_start) < 2 and len(region_of_interest_end) == 4:
                region_of_interest.append(region_of_interest_end[1] - 350)
                region_of_interest.append(region_of_interest_end[1])
                region_of_interest.append(region_of_interest_end[3] - 350)
                region_of_interest.append(region_of_interest_end[3])

#            chars_and_digits = []
            for i in range(n_region_of_interest):
                
#                chars_and_digits.append(get_digits(new_file_path, digits_template, digits_thresholds, digits, 
#                                                   region_of_interest[i],
#                                                   region_of_interest[i + 1]))
#                chars_and_digits.append(get_characters(new_file_path, chars_template, chars_thresholds, chars,
#                                                       chars_x,
#                                                       chars_y,
#                                                       region_of_interest[i],
#                                                       region_of_interest[i + 1]))
#            print(chars_and_digits)
                img = Image.open(new_file_path).convert('RGBA')
                crop_image = (region_of_interest[2* i], 700, region_of_interest[2* i + 1], 900)
                region_of_interest_image = img.crop(crop_image)        
                r_o_i_file_path = "D:\\Flights\\Weather data\\Output\\" + str(region_of_interest[i]) \
                                + "_" + str(region_of_interest[i + 1]) + ".png"
                region_of_interest_image.save(r_o_i_file_path)
                ### use Tesseract to extract digits from the region of interest
                pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
                text = pytesseract.image_to_string(region_of_interest_image)
                print(text)                  
            os.remove(new_file_path)
            print(datetime.now() - time_start)

time_start = datetime.now()            
get_regions_of_interest(path_to_test_folder)
print(datetime.now() - time_start)


################################################################################################################
################################################################################################################
#### This section implements Pytorch model to recognize digits
#import torch
#import torchvision
#
#n_epochs = 100
#barch_size_train = 64
#batch_size_test = 1000
#learning_rate = 0.01
#momentum = 0.5
#log_interval = 10
#random_seed = 1
#torch.backends.cudnn.enabled = False
#torch.manual_seed(random_seed)
#
#train_loader = torch.utils.data.DataLoader(
#                torchvision.datasets.MNIST('/files/', 
#                                           train = True, 
#                                           download = True,
#                                           transform = torchvision.transforms.Compose([
#                                                   torchvision.transforms.ToTensor(),
#                                                   torchvision.transforms.Normalize((0.1307,), (0.3081,))
#                                                   ])),
#                                           batch_size = batch_size_test,
#                                           shuffle = True)
#
#test_loader = torch.utils.data.DataLoader(
#                torchvision.datasets.MNIST('/files/',
#                                           train = False,
#                                           download = True,
#                                           transform = torchvision.transforms.Compose([
#                                                   torchvision.transforms.ToTensor(),
#                                                   torchvision.transforms.Normalize((0.1307,), (0.3081,))
#                                                   ])),
#                                           batch_size = batch_size_test,
#                                           shuffle = True)
#    
#examples = enumerate(test_loader)
#batch_idx, (example_data, example_targets) = next(examples)
#example_data.shape
#
#import matplotlib.pyplot as plt
#
#fig = plt.figure()
#for i in range(6):
#    plt.subplot(2, 3, i + 1)
#    plt.tight_layout()
#    plt.imshow(example_data[i][0], cmap = 'gray', interpolation = 'none')
#    plt.title("Ground Truth: {}".format(example_targets[i]))
#    plt.xticks([])
#    plt.yticks([])
#fig
#
#### Building the network
#
#import torch.nn as nn
#import torch.nn.functional as F
#import torch.optim as optim
#
#class Net(nn.Module):
#    def __init__(self):
#        super(Net, self).__init__()
#        self.conv1 = nn.Conv2d(1, 10, kernel_size = 5)
#        self.conv2 = nn.Conv2d(10, 20, kernel_size = 5)
#        self.conv2_drop = nn.Dropout2d()
#        self.fc1 = nn.Linear(320, 50)
#        self.fc2 = nn.Linear(50, 10)
#        
#    def forward(self, x):
#        x = F.relu(F.max_pool2d(self.conv1(x), 2))
#        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
#        x = x.view(-1, 320)
#        x = F.relu(self.fc1(x))
#        x = F.dropout(x, training = self.training)
#        x = self.fc2(x)
#        return F.log_softmax(x)
#
#device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")   
#network = Net().to(device)
#optimizer = optim.SGD(network.parameters(), lr = learning_rate, momentum = momentum)
#
#
#### Training the model
#train_losses = []
#train_counter = []
#test_losses = []
#test_counter = [i * len(train_loader.dataset) for i in range(n_epochs + 1)]
#
#def train(epoch):
#    network.train()
#    for batch_idx, (data, target) in enumerate(train_loader):
#        data = data.to(device)
#        target = target.to(device)
#        optimizer.zero_grad()
#        output = network(data)
#        loss = F.nll_loss(output, target)
#        loss.backward()
#        optimizer.step()
#        if batch_idx % log_interval == 0:
#            print('Train Epoch: {} [{}/{} ({:3.2f}%)]\tLoss: {:3.2f}'.format(
#                    epoch, batch_idx * len(data), len(train_loader.dataset),
#                    10. * batch_idx / len(train_loader), loss.item()))
#            train_losses.append(loss.item())
#            train_counter.append((batch_idx*64) + ((epoch-1)*len(train_loader.dataset)))
#            torch.save(network.state_dict(), "D:\\Flights\\Weather data\\ML\\results\\model.pth")
#            torch.save(optimizer.state_dict(), "D:\\Flights\\Weather data\\ML\\results\\optimizer.pth")
#
#
#def test():
#    network.eval()
#    test_loss = 0
#    correct = 0
#    with torch.no_grad():
#        for data, target in test_loader:
#            data, target = data.to(device), target.to(device)
#            output = network(data)
#            test_loss += F.nll_loss(output, target, size_average=False).item()
#            pred = output.data.max(1, keepdim=True)[1]
#            correct += pred.eq(target.data.view_as(pred)).sum()
#    test_loss /= len(test_loader.dataset)
#    test_losses.append(test_loss)
#    print('\nTest set: Avg. loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
#            test_loss, correct, len(test_loader.dataset),
#            10. * correct / len(test_loader.dataset)))
#    
#test()
#for epoch in range(1, n_epochs + 1):
#    train(epoch)
#    test()
#    
#fig - plt.figure()
#plt.plot(train_counter, train_losses, color = 'blue')
#plt.scatter(test_counter, test_losses, color = 'red')
#
#def load_images_to_data(image_label, image_directory, features_data, label_data):
#    list_of_files = os.listdir(image_directory)
#    for file in list_of_files:
#        image_file_name = os.path.join(image_directory, file)
#        if ".png" in image_file_name:
#            img = Image.open(image_file_name).convert("L")
#            img = np.resize(img, (28, 28, 1))
#            im2arr = np.array(new_img)
#            im2arr = im2arr.reshape(1, 28, 28, 1)            
#            features_data = np.append(features_data, im2arr, axis = 0)
#
#image = "D:\\Flights\\Weather data\\ML\\Prediction\\1_1.png"
#ThImages = glob.glob("D:\\Flights\\Weather data\\ML\\Prediction\\*.png")
#for image in ThImages:
#    img = Image.open(image)
#    new_img = np.resize(img, (28, 28, 1))
#    im2arr = np.array(new_img)
#    #im2arr = im2arr.reshape(1, 28, 28, 1)
#    #im2arr = torch.tensor(im2arr)
#    with torch.no_grad():
#        output = network(im2arr)
#        print(output)
#    
#    new_img.save("D:\\Flights\\Weather data\\ML\\Digits\\0\\0_0.png")