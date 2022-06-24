from flask import Flask

# Initialize a WSGI application
app = Flask(__name__)

from app import views
