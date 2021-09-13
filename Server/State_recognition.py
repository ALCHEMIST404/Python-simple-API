# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 17:38:47 2021

@author: Ирина
"""
# -*- coding: utf-8 -*-
#######################################################################
#Sending a document with the status of a recognized object.
#######################################################################

from flask import Flask,abort,render_template,request,redirect,url_for
from flask_restful import reqparse, abort, Api, Resource
import sys
import requests
import os
import base64
import json

########################################################################################
#To work correctly with autorun, you need to specify an absolute path. For ease of modification, it is rendered as a parameter at the beginning of the file. 
########################################################################################
absolute_path = "/home/test/Desktop/Python-simple-API-main/Server/Server_1/ssd/"

class State_recognition(Resource): 
    def get(self):
        l = [] #Create a list of uploaded files
        l.append(absolute_path+"state.txt") # Putting object data into the array
        
        i = 0
        print("----")
        while i < len(l): #Sending and encoding an object to send
            image_file = open(l[i], "rb")
            encoded_string = base64.b64encode(image_file.read())
            print(encoded_string)            
            i=i+1
        
        return encoded_string.decode('utf-8') Sending an encoded file
