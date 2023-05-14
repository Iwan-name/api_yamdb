from rest_framework import filters, mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from reviews.filter import TitleFilter
from reviews.models import Category, Genre, Title
from .serializers import (CategorySerializer,
                          GenreSerializer,
                          TitlesGetSerializer,
                          TitlesPostSerializer)


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
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
    lookup_field = 'username'

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, username=self.kwargs['username'])
        return obj


class TitleViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели Title."""
    queryset = Title.objects.all()
    serializer_class = TitleFilter
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitlesGetSerializer
        return TitlesPostSerializer
