#!/usr/bin/python3
""""
A Python script that, using a REST API, for a given employee ID, returns 
information about his/her TODO list progress.
"""


import requests
import sys


def gather_user_data(emp_id):
    """
    Returns todo list information for a given employee.
    """

    employees = requests.get('https://jsonplaceholder.typicode.com/users')
    todos_list = requests.get('https://jsonplaceholder.typicode.com/todos')

    # Retrieve user name with given employee id
    emp_name = None
    for employee in employees:
        if employee.get("emp_id") == emp_id:
            emp_name = employee.get("name")
            print(emp_name)


if __name__ == "__main__":
    employee_id = sys.argv[2]
    gather_user_data(employee_id)