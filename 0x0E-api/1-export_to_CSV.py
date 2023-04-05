#!/usr/bin/python3
"""
REST API for a given employee ID,
returns information about his/her TODO list progress
and exports data in the CSV format.
"""
import requests
import csv
import sys


def get_employee_todo_list_progress(employee_id):
    """ Fetch employee data """
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    """ Fetch employee's TODO list """
    todos_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    )
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    """ Calculate TODO list progress """
    total_tasks = len(todos_data)
    done_tasks = sum(1 for task in todos_data if task["completed"])
    employee_name = employee_data["name"]

    """ Print TODO list progress """
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}): ")
    for task in todos_data:
        if task["completed"]:
            print("\t " + task["title"])

    """ Export data in CSV format """
    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()

        for task in todos_data:
            csv_writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": task["completed"],
                "TASK_TITLE": task["title"]
            })


if __name__ == "__main__":
    PrintError = "Please provide an employee ID as a command line argument."
    if len(sys.argv) < 2:
        print ("Error: {}", PrintError)
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_list_progress(employee_id)
