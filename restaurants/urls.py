from django.urls import path
from .views import restaurant_update_view

app_name = "restaurants"
urlpatterns = [
    path("<int:pk>/update/", restaurant_update_view, name="update"),
]
