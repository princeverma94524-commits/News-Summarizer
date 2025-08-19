from django.urls import path
from . import views 

urlpatterns = [
    path('', views.login_page, name='account'), 
    path("register/",views.register_page,name='register'),
]