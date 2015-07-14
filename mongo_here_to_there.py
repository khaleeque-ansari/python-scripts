__author__ = 'khaleeque'

from pymongo import MongoClient

client = MongoClient('192.168.10.100', 27017)
db = client["job_intern"]
here = db.data


client1 = MongoClient('130.211.119.14', 27017)
db1 = client1["normalization"]
there = db1.job_intern_data


for here_item in here.find():
   there.insert(here_item)