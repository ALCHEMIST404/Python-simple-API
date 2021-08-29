# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 18:19:52 2021

@author: Ирина
"""
from requests import put, get, post
import requests
import json
import base64
from client_test import client_test

CLIENT_FOLDER = "Client/" #Folder where client files are located
CLIENT_PREFIX = "http://192.168.1.3:5000/" # Server IP

def main():
    
    test = client_test(CLIENT_FOLDER, CLIENT_PREFIX) #Test method class for functional testing
    
    #сalling test methods
    test.test_get_state_recognition() #Get data from the program
    test.test_get_screenshot() # Get a photo from the camera, processed by the recognition program
    test.test_system_state() # State of the system
    test.test_BD() #Database testing
    test.test_files_transfer_to_server() #File upload testing
    
    
if __name__ == "__main__":
    main()    

