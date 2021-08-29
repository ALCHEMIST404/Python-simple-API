# Python-simple-API
### A simple set of API methods that include:

+ Send photo to client (test part API)
+ Send a screenshot of the camera
+ Upload files to server
+ System status information
+ Working with the database (test functionality)

### How to start the application:
+ To run the server, run the file "server" from the folder "server".
+ To test the client's work, open the "client" file from the "client" folder.

You can change the CLIENT_PREFIX value depending on where your server is running. By default, the server can be run on localhost: 5000.

### Setting "Server":
+ Download and unzip the archive:
https://drive.google.com/drive/folders/1iNKe1xpWTdZe5wBcW39RWfpX3fhRUyub?usp=sharing
+ The contents of the folder should be placed in: Python-simple-API/Server/ssd/

### API methods:
#### Get_photo -  Send photo to client (test part API)

Usage example: 
192.168.1.9:5000/Get_photo

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


