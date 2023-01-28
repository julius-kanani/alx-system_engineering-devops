#!/usr/bin/python3
""""
A Python script that, using a REST API, for a given employee ID, returns
information about his/her TODO list progress in a csv format.
"""

import csv
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
    file_name = "{:d}.csv".format(req_emp.get('id'))
    # print(file_name)

    # Dry run
    data_rows = []
    for task in tasks:
        data_rows.append(
                [req_emp.get('id'), req_emp.get('username'),
                    task.get('completed'), task.get('title')])

    # print(data_rows)

    # Write to csv.
    with open(file_name, "w") as csv_file:
        # create a csvwriter object
        writer = csv.writer(csv_file, delimiter=",",  quoting=csv.QUOTE_ALL)
        writer.writerows(data_rows)
    # Prepare data.
    # print(req_emp.get('id'), req_emp.get('username'))


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
        # print(type(employee_id))
        export_user_data(employee_id)
    except Exception as Error:
        print(Error)
