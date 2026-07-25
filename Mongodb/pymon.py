# let's import the flask
from flask import Flask, render_template
import os # importing operating system module
import pymongo

MONGODB_URI=r"mongodb+srv://amankrmehta02_db_user:Mehta123@cluster0.6hbj5ms.mongodb.net/?appName=Cluster0"
client = pymongo.MongoClient(MONGODB_URI)

db = client.College # we can create a database like this or the second way

db.students.drop()


print(client.list_database_names())
