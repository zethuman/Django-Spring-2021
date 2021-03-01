from django.http import HttpResponse
from django.shortcuts import render
from array import *

from main.models import Tasks, Lists

headers = ['Task', 'Created', 'Due on', 'Owner', 'Mark' ]

lists = Lists.objects.all()
tasks = Tasks.objects.all()


def todo_list(request):
    context = {
        'headers': headers,
        'tasks': tasks.filter(),
        'lists': lists
    }

    return render(request, 'todo_list.html', context=context)


def todo_list_details(request, pk):
    context = {
        'headers': headers,
        'tasks': tasks.filter(mark=True).filter(lists_id__exact=pk),
        'lists': lists
    }

    return render(request, 'todo_list.html', context=context)


def completed_todo_list(request, pk):
    context = {
        'headers': headers,
        'completed_tasks': tasks.filter(lists_id__exact=pk).filter(mark=False),
        'lists': lists
    }

    return render(request, 'completed_todo_list.html', context=context)


