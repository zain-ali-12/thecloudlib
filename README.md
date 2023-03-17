# TheCloudlib Web App
The code contains the server of TheCloudlib web app that should be run using a WSGI server. It includes the webpages, database and backend for the web app.

## Setting up the server

Install the required packages to run the server using the command listed below

For Windows<br>
`pip install -r requirements.txt`

For Linux<br>
`pip3 install -r requirements.txt`

## Running the server

To run the server `app.py` must be run.
It can be run using the command line with the following commands

For Windows<br>
`python app.py`

For Linux<br>
`python3 app.py`

## Debugging
By default, the server does not run in debug mode. 

To run the server in debug mode add the `--debug` flag when running the python program.

eg.
`python app.py --debug`
