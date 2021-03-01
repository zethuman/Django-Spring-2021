from django.urls import path, re_path

from main.views import todo_list, completed_todo_list,  todo_list_details

urlpatterns = [
    # path('time/plus/', time_plus),
    # path('time/plus/<int: hours>', hours_ahead),
    path('', todo_list, name='todos'),
    path('todos/', todo_list, name='todos'),
    path('todos/<int:pk>/', todo_list_details, name='list-details'),
    path('todos/<int:pk>/completed/', completed_todo_list, name='completed')
]
