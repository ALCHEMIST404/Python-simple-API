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

#Server status    
class Server_state(Resource):
    def get(self):
        return "Sysytem works"