from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import *
from . import views
app_name = 'api'
urlpatterns = [
    path('course/', teacherView.as_view() ),
    path('star/', Star.as_view() ),
    path('college/', CoursesViews.as_view() ),
    path('addToCart/', AddToCArt.as_view() ),
    path('Cart/', CartView.as_view() ),
    path('teachers/', teacherView.as_view() ),

] 