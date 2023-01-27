#!/usr/bin/python3
""""
A Python script that, using a REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""


import re
import requests
import sys


def gather_user_data(emp_id):
    """
    Returns todo list information for a given employee.
    """

    # parse requests input
    REST_API = "https://jsonplaceholder.typicode.com"

    employee = "{}/users/{}".format(REST_API, emp_id)
    emp_todos = "{}/todos".format(REST_API)

    # get employee with todos list.
    req_emp = requests.get(employee).json()
    req_emp_todos = requests.get(emp_todos).json()

    # Clean the data, and filter only specified employee id.
    tasks = list(filter(lambda x: x.get('userId') == emp_id, req_emp_todos))
    number_of_tasks = len(tasks)
    # print(tasks)

    # Obtain number of completed tasks
    t_completed = list(filter(lambda task: task.get('completed'), tasks))
    no_of_task_completed = len(t_completed)

    # print(t_completed)
    # print(no_of_task_completed)
    # print(number_of_tasks)

    # Display the Emp name is done with tasks(completed/total_number)
    print("Employee {} is done with tasks({}/{}):".format(
        req_emp.get('name'), no_of_task_completed, number_of_tasks))

    # Print and display the title of the completed tasks.
    for task in t_completed:
        print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    try:
        employee_id = int(sys.argv[1])
        # print(type(employee_id))
        gather_user_data(employee_id)
    except Exception as Error:
        pass
