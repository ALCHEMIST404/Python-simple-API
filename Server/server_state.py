# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 01:40:21 2021

@author: Ирина
"""
from flask import Flask,abort,render_template,request,redirect,url_for
from flask_restful import reqparse, abort, Api, Resource
import sys
import requests
import os

########################################################################################
#To work correctly with autorun, you need to specify an absolute path. For ease of modification, it is rendered as a parameter at the beginning of the file. 
########################################################################################

absolute_path = "/home/test/Desktop/Germany/Python-simple-API-main/Server/Server_1/ssd/"

#Server status    
class Server_state(Resource):
    def get(self):
	#Collecting system state
        str_state = 'System works' # Information that the system is working correctly and turned on
        f = open(absolute_path + "system_state_status.txt", 'r') # Information about the operation of the camera, which can be taken from the monitoring log
        str_state = str_state + '\n' + "State of camera:" + f.read()

        return str_state #return all information about the system
