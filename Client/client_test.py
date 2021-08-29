# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 01:16:19 2021

@author: Ирина
"""
from requests import put, get, post
from flask_restful import reqparse, abort, Api, Resource
import requests
import json
import base64
import sys


class client_test:
    def __init__(self, CLIENT_FOLDER, CLIENT_PREFIX):
        """
        Calling Test Methods
        @params:
            CLIENT_FOLDER        - Required  : сlient file location (Str)
            CLIENT_PREFIX        - Required  : сlient IP (Str)
        """
        self.CLIENT_FOLDER = CLIENT_FOLDER # Client's content folder
        self.CLIENT_PREFIX = CLIENT_PREFIX # Client's IP
        
    #Recognition process data
    def test_get_state_recognition(self):
        print("------------test_get_state_recognition------------")
        method_url = self.CLIENT_PREFIX + 'Get_State_recognition' # API method used
        data={} # Request data
        response = requests.get(method_url, data) # Server request
        
        result = json.loads(response.text) # Query Result
        result1 = base64.b64decode(result.encode('utf-8')) # Decoding the result

        # Creating an image file
        img_file = open(self.CLIENT_FOLDER + "state.txt", 'wb')
        img_file.write(result1)
        img_file.close()
        print("Recognition state received and saved")
        
    #Getting a screenshot of the recognition program
    def test_get_screenshot(self):
        print("------------test_get_screenshot------------")
        method_url = self.CLIENT_PREFIX + 'Get_screen' # API method used
        data={} # Request data
        response = requests.get(method_url, data) # Server request
        
        result = json.loads(response.text) # Query Result
        result1 = base64.b64decode(result.encode('utf-8')) # Decoding the result

        # Creating an image file
        img_file = open(self.CLIENT_FOLDER + "state.png", 'wb')
        img_file.write(result1)
        img_file.close()
        print("Image received and saved")
        
    #Checking the status of the system
    def test_system_state(self):
        print("------------test_system_state------------")
        method_url = self.CLIENT_PREFIX + 'Server_state' # API method used
        data={} # Request data
        response = requests.get(method_url, data) # Server request
        result = json.loads(response.text) # Query Result
        print(result)
    
    #Testing a small database
    def test_BD(self):
        print("-----------------test_BD------------------")
        method_url = self.CLIENT_PREFIX + 'todos' # API method used
        data={'task': 'something new'}  # Request data
        response = requests.post(method_url, data) # Server request
        result = json.loads(response.text) # Query Result
        print(result)
        
    #Transferring many files
    def test_files_transfer_to_server(self):
        print("------test_files_transfer_to_server-------")
        
        l = [] # list of files to send
        
        method_url = self.CLIENT_PREFIX + 'File_down' # API method used
        
        #list of files to be sent
        l.append(self.CLIENT_FOLDER + '1.jpg')
        l.append(self.CLIENT_FOLDER + '2.jpg')
        l.append(self.CLIENT_FOLDER + 'test.docx')
        l.append(self.CLIENT_FOLDER + 'test.xlsx')
        l.append(self.CLIENT_FOLDER + 'test.mp4')
        
        i = 0
        
        # sending files
        while i < len(l):
            image_file = open(l[i], "rb") # opening a file
            encoded_string = base64.b64encode(image_file.read()) # String encoding to send to server
            data={'img': encoded_string, 'file_name': str(l[i])} # Request data
    
            response = requests.post(method_url, data) # Server request
            result = json.loads(response.text) #Query Result
            print(result)
            
            i=i+1
            
    
        