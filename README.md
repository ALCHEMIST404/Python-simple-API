# Python-simple-API
### A simple set of API methods that include:

+ Sending a document with recognition information.
+ Send a screenshot of the camera.
+ Upload files to server.
+ System status information.
+ Working with the database (test functionality).

### To control the operation of the system, added:
+ auto boot at power on
+ server start
+ neural network launch
+ monitoring system launch

### How to start the application:
+ To run the server, run the file "server" from the folder "server".
+ To test the client's work, open the "client" file from the "client" folder.

You can change the CLIENT_PREFIX value depending on where your server is running. By default, the server can be run on localhost: 5000.

### Setting "Server":
+ Download and unzip the archive:
https://drive.google.com/drive/folders/1iNKe1xpWTdZe5wBcW39RWfpX3fhRUyub?usp=sharing (old. 3 labels)

+ The contents of the folder should be placed in: Python-simple-API/Server/ssd/

### API methods:
#### Get_State_recognition -  Sending a document with recognition information

Usage example: 
192.168.1.9:5000/Get_State_recognition

Saves the photo on the client in the "Client" folder

#### Get_screen - Send to client a screenshot of the camera

Usage example: 
192.168.1.9:5000/Get_screen

Send to the client a screenshot taken by the server's webcam

#### File_down - Upload files to server

Usage example: 
192.168.1.9:5000/Get_screen_file

Where file is the base64.b64encode(file.read())
 
#### Server_state - System status information

Usage example: 
192.168.1.9:5000/Server_state

Will display the current information about the state of the server

#### Stubs for methods that organize the work of the database
+ todos - Working with the database (test functionality)
+ todos/<todo_id> - Working with the database (test functionality)


