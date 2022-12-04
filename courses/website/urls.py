from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import *
from . import views
app_name = 'pages'
urlpatterns = [
    path('', index.as_view(), name="index"),
    path('login', Login.as_view(), name="login"),
    path('logout', Logout.as_view(), name="logoutt"),
    path("restPassword/<str:uidb64>/<str:token>/",  RestPassword.as_view() , name="restPassword"),


] 