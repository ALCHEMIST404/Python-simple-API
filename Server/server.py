# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 18:16:40 2021

@author: Ирина
"""

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import server_uploading_files #import Img_down
from BD_server import Todo, TodoList
from server_state import Server_state
from server_sending_files import TEST_Server_state

app = Flask(__name__)
api = Api(app)



# Actually setup the Api resource routing here
api.add_resource(TEST_Server_state, '/Get_photo')
api.add_resource(server_uploading_files.File_down, '/File_down')
api.add_resource(Server_state, '/Server_state')
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
