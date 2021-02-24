from django.http import HttpResponse
from django.shortcuts import render
from array import *

headers = [
    'Task',
    'Created',
    'Due on',
    'Owner',
    'Mark'
]

task0 = {"id": 0, "task": 'Task 0', "created": '10/09/2018', 'due': '12/09/2018', "owner": 'admin', "mark": False}
task1 = {"id": 1, "task": 'Task 1', "created": '10/09/2018', 'due': '12/09/2018', "owner": 'admin', "mark": True}
task2 = {"id": 2, 'task': 'Task 2', "created": '10/09/2018', 'due': '12/09/2018', "owner": 'admin', "mark": True}
task3 = {"id": 3, 'task': 'Task 3', "created": '10/09/2018', 'due': '12/09/2018', "owner": 'admin', "mark": True}
task4 = {"id": 4, 'task': 'Task 4', "created": '10/09/2018', 'due': '12/09/2018', "owner": 'admin', "mark": True}
task5 = {"id": 0, "task": 'Task 5', "created": '10/09/2018', 'due': '12/09/2018', "owner": 'admin', "mark": False}

tasks = [task1, task2, task3, task4, task0, task5]
undone_tasks = []
done_tasks = []

for item in tasks:
    if not item['mark']:
        undone_tasks.append(item)
    else:
        done_tasks.append(item)


def todo_list(request):
    context = {
        'headers': headers,
        'tasks': done_tasks,
    }

    return render(request, 'todo_list.html', context=context)


def completed_todo_list(request):
    context = {
        'headers': headers,
        'completed_tasks': undone_tasks
    }

    return render(request, 'completed_todo_list.html', context=context)
