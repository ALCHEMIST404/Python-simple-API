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
		file_name = 'filename.png'
		File_work.make_scrin()

		file_for_send = []
		file_for_send.append(file_name)
		return File_work.send_file(file_for_send)


