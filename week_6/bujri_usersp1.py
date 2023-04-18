"""
  title: bujri_usersp1.py
  author: ngi bujri
  date: april 18 2023
  description: assignment 6.3 - python with MongoDB
"""

# import MongoClient
from pymongo import MongoClient

# MongoDB connection string
conn = "mongodb+srv://web335_user:s3cret@bellevueuniversity.hyveuqd.mongodb.net/web335DBretryWrites=true&w=majority"

# create client and connect to server
client = MongoClient(conn)

# ping server to test connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# set database to access
db = client["web335DB"]

# print all users
for user in db.users.find():
    print(f"{user}\n")

# print user with employeeID 1011
print(f"{db.users.find_one({'employeeId': '1011'})}\n")

# print user with lastName Mozart
print(db.users.find_one({"lastName": "Mozart"}))