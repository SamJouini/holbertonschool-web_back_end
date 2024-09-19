#!/usr/bin/env python3
"""Python script that provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')

    logs_collection = client.logs.nginx

    total = logs_collection.count_documents({})
    print(f"{total} logs")

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = logs_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = logs_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_check} status check")