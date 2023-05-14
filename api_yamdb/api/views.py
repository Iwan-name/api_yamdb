from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from api.serializers import UserSerializer
from users.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination


