from flask import Flask,abort,render_template,request,redirect,url_for
from flask_restful import reqparse, abort, Api, Resource
import sys
import requests
import os
from flask import Flask,abort,render_template,request,redirect,url_for
from flask_restful import reqparse, abort, Api, Resource
import sys
import requests
import os
import base64


class File_work():
	def make_scrin():
		os.system("wmctrl -a ssd-mobilenet-v2 | Network 40 FPS")
		os.system("gnome-screenshot -w -f filename.png")
		#return "OK"
	
	def send_file(l):
		print("------test_skrin_transfer_to_client-------")
		
		i = 0
		print("----")
		while i < len(l):
		    image_file = open(l[i], "rb")
		    encoded_string = base64.b64encode(image_file.read())
		    print(encoded_string)
		    
		    i=i+1
		
		return encoded_string.decode('utf-8') #.encode('utf-8')
