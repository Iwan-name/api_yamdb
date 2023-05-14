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
