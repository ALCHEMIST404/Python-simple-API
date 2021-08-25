# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 17:38:47 2021

@author: Ирина
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 01:09:38 2021

@author: Ирина
"""
from flask import Flask,abort,render_template,request,redirect,url_for
from flask_restful import reqparse, abort, Api, Resource
import sys
import requests
import os
import base64
import json
#Server status    

#ОТПРАВКА
SERVER_FOLDER = "Server/"

class TEST_Server_state(Resource):
        
    def get(self):
    #    return "Sysytem works"
        
        print("------test_files_transfer_to_client-------")
            
        l = []

        #method_url = SERVER_PREFIX + 'File_down'
        l.append(SERVER_FOLDER + '2.jpg')
        
        i = 0
        print("----")
        while i < len(l):
            image_file = open(l[i], "rb")
            encoded_string = base64.b64encode(image_file.read())
            print(encoded_string)
            
            #data={'img': encoded_string, 'file_name': str(l[i])}
            
            #encoded = base64.b64encode(image_file.encode('utf-8'))  #1 way
            #response = requests.post(method_url, data)
            #result = json.loads(response.text)
            #print(result)
            
            i=i+1
        
        return encoded_string.decode('utf-8') #.encode('utf-8')