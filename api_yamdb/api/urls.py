from django.urls import include, path

app_name = 'api'

urlpatterns = [
    path('v1/auth/signup/', APIGetToken.as_view()),
    path('v1/auth/token/', token)

]