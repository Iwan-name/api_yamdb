from django.urls import path, include

from .views import CategoryViewSet, GenreViewSet, TitleViewSet

from rest_framework import routers

app_name = 'api'

router = routers.DefaultRouter()
router.register('Category', CategoryViewSet, basename='Category')
router.register('Genre', GenreViewSet, basename='Genre')
router.register('Title', TitleViewSet, basename='Title')

urlpatterns = [
    path('v1', include(router.urls))
from django.urls import include, path
from rest_framework import routers

from api.views import UserViewSet

app_name = 'api'
router = routers.DefaultRouter()

router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    # path('v1/auth/signup/', ),
    # path('v1/auth/token/', )
    path('v1/', include(router.urls))
]
