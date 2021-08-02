from django.urls import path

from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view(redirect_authenticated_user=True), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
]
