from flask import Flask,abort,render_template,request,redirect,url_for
from flask_restful import reqparse, abort, Api, Resource
import sys
import requests
import os
import base64


class File_work():
    
    # Take a screenshot of the system
	def make_screen():
		os.system("wmctrl -a ssd-mobilenet-v2 | Network 40 FPS")
		os.system("gnome-screenshot -w -f filename.png")
	
    # Sending files to the client
    # file - the file that we send to the client
	def send_file(file):
		print("------test_screen_transfer_to_client-------")

		image_file = open(file, "rb") # opening a file
		encoded_string = base64.b64encode(image_file.read()) # File encoding to send to client
		
		return encoded_string.decode('utf-8')  #pass the encoded string
