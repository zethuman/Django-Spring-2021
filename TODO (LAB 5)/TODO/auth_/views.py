from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from auth_.models import MainUser
from auth_.serializers import UserSerializer, PasswordSerializer


class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = MainUser.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return UserSerializer
        elif self.action == 'list':
            return UserSerializer

    @action(methods=['POST'], detail=False, permission_classes=(AllowAny,))
    def post_user(self, request):
        user = request.data
        queryset = MainUser.objects.create_user(email=user['email'], password=user['password'], first_name=user['first_name'], last_name=user['last_name'])
        queryset.save()
        return Response(user, status=status.HTTP_201_CREATED)
