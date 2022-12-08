from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import *
from . import views
app_name = "pages"
urlpatterns = [
    path('', index.as_view(), name="index"),
    path('login', Login.as_view(), name="login"),
    path('logout', Logout.as_view(), name="logout"),
    path("restPassword/<str:uidb64>/<str:token>/",  RestPassword.as_view() , name="restPassword"),
    path('Teacherforms', Forms.as_view(), name="forms"),
    path('CatForm', CatCoursesForm.as_view(), name="CatForm"),
    path('Phone', Phone.as_view(), name="Phone"),
    path('CatUpdate/<int:id>/', updateCatCoursesForm.as_view(), name="Update"),
    path('TeacherUpdate/<int:id>/', updateTeacher.as_view(), name="UpdateTeacher"),
    path('Video', VideoView.as_view(), name="Video"),
    path('VideoUpdate/<int:id>/', updateVideo.as_view(), name="UpdateVideo"),
    path('VideoDelete/<int:id>/', DeleteVideo.as_view(), name="DeleteVideo"),
    path('TeacherDelete/<int:id>/', DeleteTeacher.as_view(), name="DeleteTeacher"),
    path('CourseDelete/<int:id>/', DeleteCatCourse.as_view(), name="DeleteCatCourse"),
    path('Puy/<int:id>/', bay.as_view(), name="puy"),
    path('Bannarsforms', BannarView.as_view(), name="Bannars"),
    path('BannarDelete/<int:id>/', DeleteBanars.as_view(), name="DeleteBannars"),
    


] 
handler404 = 'website.views.page_not_found_view'
handler505 = 'website.views.page_not_found_view_505'
