# Chat-App
This is a Web-based application created with Python Flask framework and utilizing HTML templates, CSS, and Javascript to simulate a chat or messaging application

To run this application locally you will need to follow the installation and usage instructions below

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/cli/pip_install/) to install the virtual environment, flask, and sqlalchemy

#### To install and activate the virtual environment:
```bash
pip install virtualenv
```
```bash
virtualenv env 
```
To activate for Mac: 
```bash
source env/bin/activate
```
To activate for Windows : 
```bash
\env\Scripts\activate.bat
```
It is important to install and activate the virtual environment because it ensures that any of the requirements or packages we install will be contained inside this environment so the project can be transferred easily

#### To install flask and sqlalchemy:
```bash
pip install flask flask-sqlalchemy
```

## Usage

Make sure to start an interactive python shell in order to setup the database

#### To start the python shell type:
```bash
python
```
Then, once in the shell, to setup the db type, line by line:
```bash
from chat_app import db
```
```bash
db.create_all()
```
```bash
exit()
```
Once this is all setup you should be ready to start the server and run the application

#### To run the application type:
```bash
python chat_app.py
```
Once you have completed these steps and run the you should see a link for a port on your local host, most likely, http://127.0.0.1:5000/, that should take you to a local deployment of the application

## Please Note:

If you are on a mac with python already installed it may not have the right version(python 3) so you will need to make sure to install the right [version](https://www.python.org/downloads/)

You will also then need to make sure to replace every pip or python command with: 
``` pip3``` or ``` python3``` 

You may also want to delete files: ``` __pycache__```, ``` app.db```, ``` chat.db```


