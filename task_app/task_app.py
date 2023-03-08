import csv
import sys
import datetime
import os
args = sys.argv
def task_read():
    with open("tasks/tasks.csv","r") as f:
        reader = csv.reader(f)
        tasks = [row for row in reader]
        return tasks
def task_add(to_do,time):
    try:
        time = datetime.datetime.strptime(time,'%Y-%m-%d')
    except:
        print("format error. format is 'Y-m-d'")
        sys.exit()
    with open("tasks/tasks.csv","a") as f:
        writer = csv.writer(f)
        writer.writerow([to_do,time])
def task_remove(delete_row):
    if delete_row > len(task_read()) or delete_row == 0:
        print("Error.No task.")
    else:
        delete_row = delete_row - 1
        with open('tasks/tasks.csv', 'r') as f:
            reader = csv.reader(f)
            rows = []
            for i, row in enumerate(reader):
                if i != delete_row:
                    rows.append(row)
        with open('tasks/tasks.csv', 'w') as f:
            writer = csv.writer(f)
            for row in rows:
                writer.writerow(row)
        print("remove.")
def task_cal():
    tasks = task_read()
    dt_now = datetime.datetime.now()
    now = datetime.datetime(dt_now.year,dt_now.month,dt_now.day)
    foundlist = []
    for t in tasks:
        if str(t[1]) == str(now):
            foundlist.append(t)
    return foundlist
def default_start():
    if os.path.exists("tasks"):
        pass
    else:
        os.mkdir("tasks")
        with open("tasks/tasks.csv","w") as f:
            pass
def autostart():
    default_start()
    if len(args) == 1:
        print("Hello")
        today_todo = task_cal()
        if len(today_todo) > 0:
            print("Today's Task")
            for t in today_todo:
                print("  Do:",t[0])
        else:
            print("Not found Today's task")
    else:
        if args[1] == "-add":
            task_add(args[2],args[3])
        elif args[1] == "-show":
            tasks = task_read()
            for t in tasks:
                print("Do:",t[0],"When:",t[1])
        elif args[1] == "-remove":
            task_remove(int(args[2]))
        else:
            print("No found command")
