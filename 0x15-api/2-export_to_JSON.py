#!/usr/bin/python3
"""Exports tasks information of an employee in csv format"""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    all_tk = requests.get(
        url + "todos", params={'userId': user_id}).json()
    username = user['username']

    with open(user_id + ".json", 'w') as f:

        json_data = {user_id: []}
        for t in all_tk:
            tmp_data = json_data[user_id]
            tmp_data.append({
                'task': t['title'],
                'completed': t['completed'],
                'username': username
                })
            json_data[user_id] = tmp_data
        json.dump(json_data, f)
