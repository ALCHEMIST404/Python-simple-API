# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 01:16:19 2021

@author: Ирина
"""
from requests import put, get, post
import requests
import json
import base64

class client_test:
    def __init__(self, CLIENT_FOLDER):
        """
        Calling Test Methods
        @params:
            CLIENT_FOLDER        - Required  : сlient file location (Str)
        """
        self.CLIENT_FOLDER = CLIENT_FOLDER
        
        
    #Checking the status of the system
    def test_system_state():
        method_url = 'http://localhost:5000/Server_state'
        data={}
        response = requests.get(method_url, data)
        result = json.loads(response.text)
        print(result)
    
    #Testing a small database
    def test_BD():
        method_url = 'http://localhost:5000/todos' 
        data={'task': 'something new'}
        response = requests.post(method_url, data)
        result = json.loads(response.text)
        print(result)
        
    #Transferring many files
    def test_files_transfer_to_server(self):
        l = []
        
        method_url = 'http://localhost:5000/File_down'
        
        l.append(self.CLIENT_FOLDER + '1.jpg')
        l.append(self.CLIENT_FOLDER + '2.jpg')
        l.append(self.CLIENT_FOLDER + 'test.docx')
        l.append(self.CLIENT_FOLDER + 'test.xlsx')
        
        i = 0
        
        while i < len(l):
            image_file = open(l[i], "rb")
            encoded_string = base64.b64encode(image_file.read())
            data={'img': encoded_string, 'file_name': str(l[i])}
    
            response = requests.post(method_url, data)
            result = json.loads(response.text)
            print(result)
            
            i=i+1
        