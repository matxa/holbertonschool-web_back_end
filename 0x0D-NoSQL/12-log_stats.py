#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
nginx = client.logs.nginx
method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print("{} logs".format(nginx.count()))

for request_type in method:
    print("\tmethod {}: {}".format(
        request_type, nginx.find({"method": request_type}).count()))
print("{} status check".format(nginx.find({"path": "/status"}).count()))
