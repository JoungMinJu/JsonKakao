from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns = [
    path('signup/', views.UserCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    # api-aut/login/, # api-auth/logout/ 다된다
]