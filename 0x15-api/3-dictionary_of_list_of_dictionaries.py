#!/usr/bin/python3
"""Exports tasks information of an employee in csv format"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", 'w') as f:
        json_data = {}
        for u in users:
            user_data = []
            user_id = u['id']
            username = u['username']
            all_tk = requests.get(
                url + "todos", params={'userId': user_id}).json()
            for t in all_tk:
                user_data.append({
                    'username': username,
                    'task': t['title'],
                    'completed': t['completed']
                    })
            json_data[user_id] = user_data

        json.dump(json_data, f)
