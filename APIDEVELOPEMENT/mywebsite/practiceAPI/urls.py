from django.contrib import admin
from django.urls import path
from practiceAPI.views import mytestcrud,abc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mytestcrud/',mytestcrud),
    path('abc/',abc)
]
