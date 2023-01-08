from django.urls import path, include
from rest_framework import routers

from student_app.views import home, StudentViewSet, studentCreate, studentDelete, studentList, studentUpdate

router = routers.DefaultRouter()
router.register("students", StudentViewSet)

urlpatterns = [
    path("", home, name="home"),
    path("automatic-api/", include(router.urls)),

	path('student-list/', studentList, name="student-list"),
	path('student-create/', studentCreate, name="student-create"),
	path('student-update/<str:pk>/', studentUpdate, name="student-update"),
	path('student-delete/<str:pk>/', studentDelete, name="student-delete"),
]