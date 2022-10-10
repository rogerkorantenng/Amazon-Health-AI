# Amazon-Health-AI

This app is built with Flask, using trained models

This project contains a folder and two files namely(requirements.txt and app.py). The folder cantains the template index.html

The index.html file serves as the template for the app and is rendered to the flask app through Jinja2

The app.py conatains the actual code

The requirements.txt contains a list of all python libraries to be installed

The model folder contains the jupyter notebook file which was saved from Sagemaker studio's after training
How to Install Locally

Before running the app.py file its required of you to install all python libraries listed in the requirement.txt file. To install the python libraries, you first need to install pip, pip3 is a standard package manager for python

To install pip on windows visit https://www.w3schools.com/python/python_pip.asp

To install pip on linux vist https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/

To install pip on mac visit https://phoenixnap.com/kb/install-pip-mac

After successfully installing pip, we can now use pip to install libraries in the requirements.txt by running the below command in our terminal

pip3 install -r requirements.txt

After successfully installing all python libraries through pip, you can now run the application

Open terminal and navigate to the folder or path where the files are kept and type the code below

sudo python3 main.py, this opens your web browser on localhost and port 88.

In the case you rceieve an error OSError: [Errno 98] Address already in use, change the port in the last line of the code to your desired port
Production Use

For production use 'only' add host='0.0.0.0' to the last line
Testing

The app was tested on a Linux Ubuntu and Linux Mint
Access Live Site Via

http://insuranceapp.rogerkoranteng.com
