#!/usr/bin/python3
"""
REST API for a given employee ID,
returns information about his/her TODO list progress
and exports data in the CSV format.
"""
import requests
import sys
import csv
import os

EMPLOYEE_ENDPOINT = "https://jsonplaceholder.typicode.com/users/{}/"
TODO_ENDPOINT = "https://jsonplaceholder.typicode.com/todos?userId={}"


def get_employee_todo_progress(employee_id):
    """grabs employee todo progress"""
    employee_response = requests.get(EMPLOYEE_ENDPOINT.format(employee_id))
    employee_data = employee_response.json()
    employee_name = employee_data['username']

    todo_response = requests.get(TODO_ENDPOINT.format(employee_id))
    todo_data = todo_response.json()

    total_tasks = len(todo_data)
    completed_tasks = 0
    completed_task_titles = []

    for task in todo_data:
        if task['completed']:
            completed_tasks += 1
            completed_task_titles.append(task['title'])

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_tasks, total_tasks))
    for title in completed_task_titles:
        print("\t ", title)

    with open('{}.csv'.format(employee_id), 'w', encoding='utf-8',
              newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_MINIMAL,
                            lineterminator=os.linesep)
        for task in todo_data:
            writer.writerow([employee_id, employee_name,
                             str(task['completed']).lower(), task['title']])


if __name__ == '__main__':
    if len(sys.argv) == 2:
        employee_id = sys.argv[1]
        get_employee_todo_progress(employee_id)
    else:
        print("Usage: python script_name.py <employee_id>")
