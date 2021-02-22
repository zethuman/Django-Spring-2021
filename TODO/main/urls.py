from django.urls import path, re_path

from main.views import todo_list, completed_todo_list

urlpatterns = [
    # path('time/plus/', time_plus),
    # path('time/plus/<int: hours>', hours_ahead),
    path('todos/', todo_list),
    path('todos/1/completed/', completed_todo_list)
]
