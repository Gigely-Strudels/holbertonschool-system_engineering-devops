#!/usr/bin/python3
"""dictionary of list of dictionaries"""
import json
import requests
import hashlib

base_url = "https://jsonplaceholder.typicode.com"


def get_employee_list():
    """grabs employee list"""
    employee_response = requests.get("{}/users".format(base_url))
    employee_data = employee_response.json()

    return employee_data


def get_employee_task_list(employee_id, username):
    """grabs employee task list"""
    todo_response = requests.get("{}/users/{}/todos"
                                 .format(base_url, employee_id))
    todo_data = todo_response.json()

    task_data = []
    for task in todo_data:
        task_data.append({
            "username": username,
            "task": task['title'],
            "completed": task['completed']
        })

    return task_data


def export_to_json(employee_data_list):
    """export to json"""
    file_name = "todo_all_employees.json"

    task_list = {}
    for employee in employee_data_list:
        employee_id = employee['id']
        username = employee['username']
        tasks = get_employee_task_list(employee_id, username)
        task_list[employee_id] = tasks

    with open(file_name, 'w') as jsonfile:
        json.dump(task_list, jsonfile)

    print("Data exported to {}".format(file_name))


if __name__ == "__main__":
    employee_data_list = get_employee_list()
    export_to_json(employee_data_list)
