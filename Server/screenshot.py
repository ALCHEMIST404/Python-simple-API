######################################################################
#This method takes a screenshot of the running recognition application and sends it to the client.
######################################################################

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
from files_and_images import File_work

class Screenshot(Resource):
	def get(self):
		file_name = 'filename.png' #Screenshot name to save on the server
		File_work.make_scrin() # Screenshot of the desired area

		file_for_send = [] #Array of files to send (we use the method of sending multiple images for sending)
		file_for_send.append(file_name) #Adding a screenshot for sending
		return File_work.send_file(file_for_send) #Sending a screenshot to the user
