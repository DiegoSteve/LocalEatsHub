from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("landing.urls", namespace="landing")),
    path("users/", include("users.urls", namespace="users")),
    path("dishes/", include("dishes.urls", namespace="dishes")),
    path("restaurants/", include("restaurants.urls", namespace="restaurants")),
    path("students/", include("students.urls", namespace="students")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
