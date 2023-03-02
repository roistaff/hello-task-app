import csv
import sys
import datetime
args = sys.argv
def task_read():
    with open("tasks.csv","r") as f:
        reader = csv.reader(f)
        tasks = [row for row in reader]
        return tasks[1][0]
def task_add(to_do,time):
    with open("tasks.csv","a") as f:
        writer = csv.writer(f)
        writer.writerow([to_do,time])
def task_remove(delete_row):
    with open('tasks.csv', 'r') as f:
        reader = csv.reader(f)
        rows = []
        for i, row in enumerate(reader):
            if i != delete_row:
                rows.append(row)
    with open('tasks.csv', 'w') as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)
def default_start():
    print("hello")
def autostart():
    if len(args) != 1:
        print("Hello")