from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from api.views import UserViewSet, UserCreateViewSet, UserReceiveTokenViewSet
from .views import CategoryViewSet, GenreViewSet, TitleViewSet
from .views import (
    CommentViewSet,
    ReviewViewSet
)

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='Category')
router.register(r'genres', GenreViewSet, basename='Genre')
router.register(r'titles', TitleViewSet, basename='Title')
router.register(r'users', UserViewSet, basename='users')
auth_urls = [
    path(
        'signup/',
        UserCreateViewSet.as_view({'post': 'create'}),
        name='signup'
    ),
    path(
        'token/',
        UserReceiveTokenViewSet.as_view({'post': 'create'}),
        name='token'
    )
]

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include(auth_urls)),
]

router_v1 = DefaultRouter()
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
