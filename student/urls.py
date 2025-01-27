from django.urls import path 
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('studentsignup', views.student_signup_view,name='studentsignup'),
    path('account/', views.studentDashboard, name='student-dashboard'),
    path('student_profile/', views.studentProfile, name='student-profile'),
]