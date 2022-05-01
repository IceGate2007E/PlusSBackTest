import re
from this import d
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status, mixins, generics, viewsets
from users.serializers import UserSerializer

from users.models import User

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer



