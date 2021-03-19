from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from auth_.views import CreateUserViewSet

urlpatterns = [
    # path('time/plus/', time_plus),
    # path('time/plus/<int: hours>', hours_ahead),
    path('login/', obtain_jwt_token),
    path('signup/', CreateUserViewSet.as_view({'post': 'post_user', 'get': 'list'}))
]
