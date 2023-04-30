"""
  title: bujri_usersp2.py
  author: ngi bujri
  date: april 29 2023
  description: assignment 7.3
"""

# import MongoClient
from pymongo import MongoClient
import datetime

# MongoDB connection string
conn = "mongodb+srv://web335_user:s3cret@bellevueuniversity.hyveuqd.mongodb.net/web335DBretryWrites=true&w=majority"

# create client and connect to server
client = MongoClient(conn)

# ping server to test connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# set database to access
db = client["web335DB"]

# create new user document
db.users.insert_one(
    {
        "firstName": "first",
        "lastName": "last",
        "employeeId": "1014",
        "email": "first@me.com",
        "dateCreated": datetime.datetime.now(),
    }
)

# return the newly created document
print(db.users.find_one({"firstName": "first"}))

# update the users email
db.users.update_one({"firstName": "first"}, {"$set": {"email": "update@me.com"}})

# return updated document
print(db.users.find_one({"email": "update@me.com"}))

# delete the new user
db.users.delete_one({"firstName": "first"})

# check if document was deleted
print(db.users.find_one({"firstName": "first"}))
