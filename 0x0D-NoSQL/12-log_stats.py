#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
nginx = client.logs.nginx
method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print(nginx.count_documents({}))

for request_type in method:
    print("\tmethod {}: {}".format(
        request_type, nginx.count_documents({"method": request_type})))
print("{} status check".format(nginx.count_documents({"path": "/status"})))
