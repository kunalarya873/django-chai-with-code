from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", include('blog.urls')),
    path("authenticate/", include("authentication.urls")),
]
