#!/usr/bin/python3
"""Returns todo list progress of an employee"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    all_tk = requests.get(
        url + "todos", params={'userId': sys.argv[1]}).json()

    completed_tasks = [tk['title'] for tk in all_tk if tk['completed'] is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user['name'], len(completed_tasks), len(all_tk)))
    for title_task in completed_tasks:
        print("\t {}".format(title_task))
