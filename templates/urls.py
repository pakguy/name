from django.urls import path 
from django.contrib.auth.views import LoginView
from . import views

from .views import *
urlpatterns = [
    path('', views.home, name='home'),
    # path('', views.home_view, name='home'),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('examroom/<int:examroom_id>/', views.invigilator_view_examroom_details, name='invigilator_examroom_details'),
    path('examroom/<int:examroom_id>/', views.view_examroom_details, name='examroom_details'),
    path('dashboard/profile/', views.adminProfile, name='admin-profile'),
    path('dashview/', views.dashview, name='dashview'),
    path('dashboard/', views.your_view, name='admin-dashboard'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('login',views.login, name='login'),
    path('invigilatorboard', views.invigilator_detail, name='invigilator_details'),

    path('create_event', create_event, name='create_event'),
    
    path('allocate_invigilator', views.admin_assign_invigilator,name='assign_invigilator'),
   
    
    
    
    path('admin-course', views.admin_course_view,name='admin-course'),
    path('add_course', views.admin_add_course_view,name='admin-add-course'),
    path('admin-view-course', views.admin_view_course_view,name='admin-view-course'),
    path('delete-course/<int:pk>', views.delete_course_view,name='delete-course'),
    
    

    path('add_exam', views.admin_add_exam,name='admin-add-exam'),
    
    
    
    path('admin_timetable', views.admin_timetable,name='admin_timetable'),
    path('admin_schedule_edit/<str:pk>', views.adminScheduleEdit_by_item, name='admin-schedule-edit-each'),
    path('schedule/delete/<str:pk>', views.deleteSchedule, name='admin-delete-schedule'),
   
    
]