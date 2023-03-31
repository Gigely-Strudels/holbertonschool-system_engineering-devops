#!/usr/bin/python3
"""
REST API for a given employee ID,
returns information about his/her TODO list progress
and exports the data to a CSV file.
"""
import requests
import sys
import csv

def get_employee_todo_progress(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code == 200 and todos_response.status_code == 200:
        user_data = user_response.json()
        todos_data = todos_response.json()
        employee_name = user_data["name"]
        
        done_tasks = [task for task in todos_data if task["completed"] == True]
        total_tasks = len(todos_data)
        
        progress_report = f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):"
        print(progress_report)

        for task in done_tasks:
            print("\t ", task["title"])

        with open(f"{employee_id}.csv", "w", newline='', encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            
            for task in todos_data:
                csv_writer.writerow([employee_id, employee_name, task["completed"], task["title"]])

    else:
        print("Error: Invalid employee ID or request failed.")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    else:
        print("Usage: python script_name.py <employee_id>")
