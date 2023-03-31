#!/usr/bin/python3
"""
REST API for a given employee ID,
returns information about his/her TODO list progress
and exports data in the CSV format.
"""
import requests
import sys
import csv

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
        print("\t {}", title)


def export_to_csv(employee_id, employee_name, todo_data):
    """exports data in the CSV format"""
    file_name = "{}.csv".format(employee_id)

    with open(file_name, 'w', encoding='utf-8', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todo_data:
            csv_writer.writerow([employee_id, employee_name,
                                 task['completed'], task['title']])

    print("Data exported to {}".format(file_name))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    employee_data, todo_data = get_employee_todo_progress(employee_id)

    if employee_data and todo_data:
        export_to_csv(employee_id, employee_data, todo_data)
