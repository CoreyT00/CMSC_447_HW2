# importing the necessary tools
from flask import Flask
import sqlite3

app = Flask(__name__)

# connecting the database to this python program
connection = sqlite3.connect('MyData.db')
cursor = connection.cursor()


@app.route("/")
def home():
    return "Hello, Flask!"
