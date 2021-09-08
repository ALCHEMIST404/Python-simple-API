# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 01:09:38 2021

@author: Ирина
"""

###################################################
#This method is planned as a test method for uploading a file to the server. It can also be called now, but at the moment it is disconnected from the server.
###################################################

from flask import Flask,abort,render_template,request,redirect,url_for
from flask_restful import reqparse, abort, Api, Resource
import sys
import requests
import os
import base64

#Parser for parameters that may come
parser_docs = reqparse.RequestParser()
parser_docs.add_argument('img')
parser_docs.add_argument('file_name')

SERVER_FOLDER = "Server/" #The folder in which you plan to save the received files
#Uploading one image
class File_down(Resource):
    def post(self):
        
        args = parser_docs.parse_args() #Parse the incoming request
        file = str(args['img']) #we clear the request and get its purpose
        try:
            file_name = str(args['file_name'].split("/")[-1])
        except Exception:
            file_name = str(args['file_name'])
        try: 
            decoded_data = base64.b64decode(file) #Decode the file to send
            img_file = open(SERVER_FOLDER + file_name, 'wb') # Opening a file for upload
            img_file.write(decoded_data) # Decoding
            img_file.close() #End of work with the file
            status = file_name + ": File uploaded to the server" #Keep a record of the status for the log
            
        except Exception:
            status = str(sys.exc_info()) #Keep a record of the status for the log
        return status
