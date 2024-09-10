from django.urls import path
from dishes.views import DishCreateView

app_name = "dishes"
urlpatterns = [
    path("add/", DishCreateView.as_view(), name="add"),
]
