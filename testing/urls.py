
from django.urls import path
from django.conf.urls import url
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('users',views.users.as_view() ),
    path('users/<int:user_id>/',views.user_info.as_view())
    
]