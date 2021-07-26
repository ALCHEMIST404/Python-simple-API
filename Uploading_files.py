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

parser_docs = reqparse.RequestParser()
parser_docs.add_argument('img')
parser_docs.add_argument('file_name')

SERVER_FOLDER = "Server/"
#Uploading one image
class File_down(Resource):
    def post(self):
        
        args = parser_docs.parse_args()
        file = str(args['img'])
        try:
            file_name = str(args['file_name'].split("/")[-1])
            status = file_name
        except Exception:
            file_name = str(args['file_name'])
            status = str(sys.exc_info())
        try: 
            decoded_data = base64.b64decode(file)
            img_file = open(SERVER_FOLDER + file_name, 'wb')
            img_file.write(decoded_data)
            img_file.close()
            status = file_name#"Image uploaded to the server"
            
        except Exception:
            status = str(sys.exc_info())
        return status
    