from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import User
from app.utils.response import response


class UserView(viewsets.ModelViewSet):
    @action(detail=False, methods=['post'])
    def login(self, request):
        account = request.data.get('account')
        password = request.data.get('password')

        code, data = User.objects.login(account, password)
        return response(code, data)

