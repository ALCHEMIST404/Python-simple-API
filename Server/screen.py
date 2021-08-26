import sys
import os
import requests
import base64

from files_and_images import File_work
from flask import Flask,abort,render_template,request,redirect,url_for
from flask_restful import reqparse, abort, Api, Resource

class Screen(Resource):
	def get(self):
		file_name = 'filename.png'
		File_work.make_scrin()
		return File_work.send_file(file_name)


