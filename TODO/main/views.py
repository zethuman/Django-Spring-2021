from django.http import HttpResponse
from django.shortcuts import render
from array import *





def todo_list(request):
    list1 = dict(
        task1=[{'task': 'Task 1', "created": '10/09/2018', 'due': '12/09/2018', "owner": 'admin', "mark": True}],
        task2=[{'task': 'Task 2', "created": '10/09/2018', 'due': '12/09/2018', "owner": 'admin', "mark": True}],
        task3=[{'task': 'Task 3', "created": '10/09/2018', 'due': '12/09/2018', "owner": 'admin', "mark": True}],
        task4=[{'task': 'Task 4', "created": '10/09/2018', 'due': '12/09/2018', "owner": 'admin', "mark": True}],
        task5=[{'task': 'Task 5', "created": '10/09/2018', 'due': '12/09/2018', "owner": 'admin', "mark": True}],)

    task1 = list1.values()

    headers = [
        'Task',
        'Created',
        'Due on',
        'Owner',
        'Mark'
    ]
    todos = {
        'tasks': list1,
        'test': task1,
        'headers': headers,
    }

    return render(request, 'todo_list.html', context=todos)


def completed_todo_list(request):
    completed_tasks = dict(
        task0=[{'task': 'Task 0', "created": '10/09/2018', 'due': '12/09/2018', "owner": 'admin', "mark": False}],
        task5=[{'task': 'Task 5', "created": '10/09/2018', 'due': '12/09/2018', "owner": 'admin', "mark": False}],)

    headers = [
        'Task',
        'Created',
        'Due on',
        'Owner',
        'Mark'
    ]
    todos = {
        'headers': headers,
        'completed_tasks': completed_tasks
    }

    return render(request, 'completed_todo_list.html', context=todos)
