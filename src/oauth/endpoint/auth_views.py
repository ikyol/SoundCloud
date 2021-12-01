from django.shortcuts import render
from rest_framework.decorators import api_view
from .. import serializer
from rest_framework.exceptions import AuthenticationFailed


def google_login(request):
    """Страница входа через Google"""
    return render(request, 'oauth/google_login.html')


@api_view(["POST"])
def google_auth(request):
    """Подтверждение авторизации через Google"""
    google_data = serializer.GoogleAuth(data=request.data)
    if google_data.is_valid():
        pass
    else:
        return AuthenticationFailed(code=403, detail='Bad data Google')
