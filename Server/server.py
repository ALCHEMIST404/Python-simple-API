# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 18:16:40 2021

@author: Irina
"""
############################################################################
#This file contains all available methods and method references to them. All new methods are added exclusively to this file.
############################################################################

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import server_uploading_files #import Img_down
from BD_server import Todo, TodoList
from server_state import Server_state
#from server_sending_files import TEST_Server_state
from screenshot import Screenshot
from State_recognition import State_recognition

app = Flask(__name__)
api = Api(app)

# Actually setup the API resource routing here

api.add_resource(Screenshot, '/Get_screen') # Send a screenshot of the camera
api.add_resource(State_recognition, '/Get_State_recognition') # Send a screenshot of the camera
api.add_resource(server_uploading_files.File_down, '/File_down') # Upload files to server
api.add_resource(Server_state, '/Server_state') # System status information
api.add_resource(TodoList, '/todos') # Working with the database (test functionality)
api.add_resource(Todo, '/todos/<todo_id>') # Working with the database (test functionality)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
