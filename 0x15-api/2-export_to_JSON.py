#!/usr/bin/python3
""""
A Python script that, using a REST API, for a given employee ID, returns
information about his/her TODO list progress in a csv format.
"""

import csv
import json
import requests
import sys


def export_user_data(emp_id):
    """
    Returns todo list information for a given employee in a csv fomart.
    """

    # parse requests input
    REST_API = "https://jsonplaceholder.typicode.com"

    employee = "{}/users/{}".format(REST_API, emp_id)
    emp_todos = "{}/todos".format(REST_API)

    # get employee with todos list.
    req_emp = requests.get(employee).json()
    # print(type(req_emp))
    req_emp_todos = requests.get(emp_todos).json()

    # Clean the data, and filter only specified employee id.
    tasks = list(filter(lambda x: x.get('userId') == emp_id, req_emp_todos))
    # number_of_tasks = len(tasks)
    # print(tasks)
    file_name = "{:d}.json".format(req_emp.get('id'))
    # print(file_name)

    # Dry run
    data_rows = []
    for task in tasks:
        data_rows.append(
                {"task": task.get('title'), "completed": task.get('completed'),
                    "username": req_emp.get('username')})

    # print(data_rows)

    # Export as json
    export_data = {"{:d}".format(req_emp.get('id')): data_rows}
    # print(type(export_data))
    # print(export_data)

    # Write to a json file.
    user_tasks = json.dumps(export_data)
    with open(file_name, "w") as json_file:
        json_file.write(user_tasks)


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
        # print(type(employee_id))
        export_user_data(employee_id)
    except Exception as Error:
        print(Error)
