# intern_assessment
To run the file following installations and environments has to be configured:
Step1: Creating a directory in pycharm
$ mkdir Src
$ cd Src
Step 2: Creating a python file 
$ touch main.py
(here the code can be fetched from main.py) 
Step 3: Creating a virtual environment and then later activate it
$ python3 -m venv env
$ source env/bin/activate
Step 4: install the flask-restful 
$ pip3 install flask-restful
Step 5: To run the python file 
$ python main.py

On running the URL http://localhost:5000/v1/sanitized/input in Postman, we get to know the output is sanitized or unsanitized for the payload input.

To run the test file command used is: 

python -m unittest discover -p test.py
