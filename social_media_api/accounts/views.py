from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model
from rest_framework import serializers

class RegisterView(APIView):
    def post(self, request):
        # Register user logic
        ...

class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        # Login logic
        ...

