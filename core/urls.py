from django.contrib import admin
from django.urls import path
from users.views import index
from visitors.views import visitor_register

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name='index'),
    path("visitor_register", visitor_register,
         name="visitor_register")
    
]
