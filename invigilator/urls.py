from django.urls import path 
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    path('invigilatorprofile',views.dashboard, name='invigilator-profile'),
    path('invigilatorsignup', views.invigilator_signup_view, name='invigilatorsignup'),
    path('invigilatorsignin', LoginView.as_view(template_name='invigilator/login.html'),name='invigilatorlogin'),

]