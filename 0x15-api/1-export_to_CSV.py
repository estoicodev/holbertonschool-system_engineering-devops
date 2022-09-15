#!/usr/bin/python3
"""Exports tasks information of an employee in csv format"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    all_tk = requests.get(
        url + "todos", params={'userId': user_id}).json()
    username = user['username']

    with open(user_id + ".csv", 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for t in all_tk:
            writer.writerow(
                [user_id, username, t['completed'], t['title']])
