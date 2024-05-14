#!/usr/bin/env python3
""" Provide statistics about Nginx logs stored in MongoDB - new version """
from pymongo import MongoClient


def nginx_stats_check():
    """ Display various statistics about Nginx logs stored in MongoDB """
    client = MongoClient()
    nginx_collection = client.logs.nginx

    total_logs_count = nginx_collection.count_documents({})
    print(f"{total_logs_count} logs")

    print("Methods:")
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in http_methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f"\tMethod {method}: {method_count}")

    status_check_count = nginx_collection.count_documents(
            {"method": "GET", "path": "/status"})
    print(f"{status_check_count} status checks")

    print("IPs:")

    top_ips = nginx_collection.aggregate([
        {"$group":
         {
             "_id": "$ip",
             "count": {"$sum": 1}
         }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])
    for top_ip in top_ips:
        count = top_ip.get("count")
        ip_address = top_ip.get("ip")
        print(f"\t{ip_address}: {count}")


if __name__ == "__main__":
    nginx_stats_check()
