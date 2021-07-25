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

#Uploading one image
class Img_down(Resource):
    def post(self):
        
        args = parser_docs.parse_args()
        file = str(args['img'])
        status = "123"
        try: 
            decoded_data = base64.b64decode(file)
            img_file = open("Server/test.jpg", 'wb')
            img_file.write(decoded_data)
            img_file.close()
            status = "Image uploaded to the server"
            
        except Exception:
            status = str(sys.exc_info())
        return status
    
    