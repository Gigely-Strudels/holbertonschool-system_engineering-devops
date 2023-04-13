#!/usr/bin/python3
"""
REST API for a given employee ID,
returns information about his/her TODO list progress
and exports data in the CSV format.
"""
import requests
import sys
import csv


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


def export_to_csv(employee_id, todo_data):
    """exports data in the CSV format"""
    file_name = "{}.csv".format(employee_id)

    with open(file_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todo_data:
            csv_writer.writerow([employee_id, employee_data['username'],
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
