from django.urls import path, include
from . import views


app_name = 'courses'


urlpatterns = [
    path('<slug:course_name>/<int:id>/', views.course, name="course"),
]
