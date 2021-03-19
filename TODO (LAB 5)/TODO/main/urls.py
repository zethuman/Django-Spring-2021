from django.urls import path, re_path
from rest_framework import routers
from main.views import ListViewSet, TaskViewSet
# router = routers.SimpleRouter()
# router.register('todos', ListViewSet, basename='main')

urlpatterns = [
    # Lists and Lists details
    path('todos/', ListViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('todos/<int:pk>/', ListViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'post': 'create',
                                                 'put': 'update'})),

    # Tasks and Tasks details
    path('tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('tasks/<int:pk>/', TaskViewSet.as_view({'get': 'retrieve', 'delete': 'destroy',
                                                 'put': 'update'})),

    # Completed and Tasks in Lists
    path('todos/<int:pk>/tasks/', ListViewSet.as_view({'get': 'tasks_by_list'})),
    path('todos/<int:pk>/completed/', TaskViewSet.as_view({'get': 'completed'})),
]

# urlpatterns += router.urls;
