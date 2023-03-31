#!/usr/bin/python3
""""""
import json
import requests
import sys
import urllib


def get_employee_todo_progress(employee_id):
    """grabs employee todo progress"""
    base_url = "https://jsonplaceholder.typicode.com"

    employee_response = requests.get("{}/users/{}"
                                     .format(base_url, employee_id))
    employee_data = employee_response.json()

    if "name" not in employee_data:
        print("Employee ID does not exist")
        return None, None

    todo_response = requests.get("{}/users/{}/todos"
                                 .format(base_url, employee_id))
    todo_data = todo_response.json()

    return employee_data, todo_data


def export_to_json(employee_id, todo_data):
    """exports data in the JSON format"""
    file_name = "{}.json".format(employee_id)
    task_data = []

    for task in todo_data:
        task_data.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_data['username']
        })

    json_data = {employee_id: task_data}

    with open(file_name, 'w') as jsonfile:
        json.dump(json_data, jsonfile)

    print("Data exported to {}".format(file_name))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    employee_data, todo_data = get_employee_todo_progress(employee_id)

    if employee_data and todo_data:
        export_to_json(employee_id, employee_data['username'], todo_data)
