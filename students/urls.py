from django.urls import path
from .views import student_update_view

app_name = "students"
urlpatterns = [
    path("<int:pk>/update/", student_update_view, name="update"),
]
