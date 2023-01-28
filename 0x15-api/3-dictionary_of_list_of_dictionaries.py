#!/usr/bin/python3
""""
A Python script that, using a REST API, for a given employee ID, returns
information about his/her TODO list progress in a csv format.
"""

import csv
import json
import requests
import sys


def export_user_data():
    """
    Returns todo list information for a given employee in a csv fomart.
    """

    # parse requests input
    REST_API = "https://jsonplaceholder.typicode.com"

    employees = "{}/users".format(REST_API)
    emp_todos = "{}/todos".format(REST_API)

    # get employee with todos list.
    req_emp = requests.get(employees).json()
    # print(req_emp)
    req_todos = requests.get(emp_todos).json()
    # print("Start", req_emp_todos)

    # Clean the data, and filter only specified employee id.
    e_tasks = {}
    for i in range(1, len(req_emp) + 1):
        e_tasks[i] = list(filter(lambda x: x.get('userId') == i, req_todos))
    # for key, value in e_tasks.items():
        # print(key, value)

    export_tasks = {}
    for key, tasks in e_tasks.items():
        user_tasks = []
        user = list(filter(lambda x: x.get('id') == key, req_emp))
        # print(user)
        name_user = None
        for item in user:
            name_user = item.get('username')
            # print(name_user)
            break
        for task in tasks:
            user_tasks.append(
                    {"username": name_user, "task": task.get('title'),
                        "completed": task.get('completed')})

        # print(key, ": ", user_tasks)
        # print(key)
        export_tasks.update({"{:d}".format(key): user_tasks})
    # Write to json file
    file_name = "todo_all_employees.json"
    export_json = json.dumps(export_tasks)
    with open(file_name, "w") as json_file:
        json_file.write(export_json)


if __name__ == "__main__":
    try:
        export_user_data()
    except Exception as Error:
        print(Error)
