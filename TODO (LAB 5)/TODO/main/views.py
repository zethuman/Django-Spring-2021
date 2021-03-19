from django.shortcuts import render
from rest_framework import viewsets, renderers, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .serializers import ListSerializer, ListDetailSerializer, TaskSerializer, TaskDetailSerializer
from main.models import Tasks, Lists

# headers = ['Task', 'Created', 'Due on', 'Owner', 'Mark' ]


class ListViewSet(viewsets.ModelViewSet):
    queryset = Lists.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'list':
            return ListSerializer
        elif self.action == 'retrieve':
            return ListDetailSerializer
        elif self.action == 'create':
            return TaskDetailSerializer
        elif self.action == 'destroy':
            return TaskDetailSerializer
        elif self.action == 'update':
            return ListSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny,))
    def tasks_by_list(self, request, pk):
        queryset = Tasks.objects.filter(lists_id=pk)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskSerializer
        elif self.action == 'retrieve':
            return TaskDetailSerializer
        elif self.action == 'create':
            return TaskDetailSerializer
        elif self.action == 'destroy':
            return TaskDetailSerializer
        elif self.action == 'update':
            return TaskDetailSerializer

    @action(methods=['GET'], detail=True, permission_classes=(AllowAny, ))
    def completed(self, request, pk):
        queryset = Tasks.objects.filter(mark=False)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)


# def todo_list(request):
#     context = {
#         'headers': headers,
#         'tasks': tasks.filter(),
#         'lists': lists
#     }
#
#     return render(request, 'todo_list.html', context=context)
#
#
# def todo_list_details(request, pk):
#     context = {
#         'headers': headers,
#         'tasks': tasks.filter(mark=True).filter(lists_id__exact=pk),
#         'lists': lists
#     }
#
#     return render(request, 'todo_list.html', context=context)
#
#
# def completed_todo_list(request, pk):
#     context = {
#         'headers': headers,
#         'completed_tasks': tasks.filter(lists_id__exact=pk).filter(mark=False),
#         'lists': lists
#     }
#
#     return render(request, 'completed_todo_list.html', context=context)


