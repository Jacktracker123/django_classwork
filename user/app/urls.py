from django.urls import path
from . import views
urlpatterns = [
    path('form/', views.add_user,name='add user'),
    path('login/',views.login_user,name='login'),
    path('home/',views.login_user,name='home')
]