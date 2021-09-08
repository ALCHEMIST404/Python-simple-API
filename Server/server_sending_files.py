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
########################################################################################
#This file is a blank for sending an unlimited number of files to the client. Not included in the test.
########################################################################################
########################################################################################
#To work correctly with autorun, you need to specify an absolute path. For ease of modification, it is rendered as a parameter at the beginning of the file. 
########################################################################################
from flask import Flask,abort,render_template,request,redirect,url_for
from flask_restful import reqparse, abort, Api, Resource
import sys
import requests
import os
import base64
import json
#Server status    

#ОТПРАВКА
SERVER_FOLDER = "/home/test/Desktop/Germany/Python-simple-API-main/Server/Server_1/Server/"

class TEST_Server_state(Resource):
        
    def get(self):

        print("------test_files_transfer_to_client-------")
            
        l = [] #List of files to send

        l.append(SERVER_FOLDER + '2.jpg') #Collecting files to send
        
        i = 0
        print("----")

        while i < len(l): # File upload cycle
            image_file = open(l[i], "rb") # Opening the file we are about to send
            encoded_string = base64.b64encode(image_file.read()) #Decoding a file to send
            print(encoded_string) # File output control line
            
            i=i+1
        
        return encoded_string.decode('utf-8') #File upload
