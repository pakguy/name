from django.urls import path 
from django.contrib.auth.views import LoginView
from . import views

from .views import *


urlpatterns = [
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('', views.home, name='home'),
    path('login',views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('examhalls', views.your_view, name='examhalls'),
    path('examroom/<int:examroom_id>/', views.view_examroom_details, name='examroom_details'),
    # path('examhall_details', views.view_examroom_details, name='examhall_details'),
    # path('examroom/<int:examroom_id>/', views.view_examroom_details, name='examroom_details'),
    path('dashboard/profile/', views.adminProfile, name='admin-profile'),
    
    
    
    path('allocate_invigilator', views.assign_invigilator,name='assign_invigilator'),
    
    
    # courses urls
    
    path('admin-course', views.admin_course_view,name='admin-course'),
    path('add_course', views.admin_add_course_view,name='admin-add-course'),
    path('admin-view-course', views.admin_view_course_view,name='admin-view-course'),
    path('delete-course/<int:pk>', views.delete_course_view,name='delete-course'),
    
    
    # timetable
    

    path('add_exam', views.admin_add_exam,name='admin-add-exam'),
    
    
    path('admin_timetable', views.admin_timetable,name='admin_timetable'),
    path('admin_schedule_edit/<str:pk>', views.adminScheduleEdit_by_item, name='admin-schedule-edit-each'),
    path('schedule/delete/<str:pk>', views.deleteSchedule, name='admin-delete-schedule'),
    # SEMICFORM URL
    path("semicform/", views.Semicform, name="semicform"),
    path("feedback/", views.feedback_form, name="feedback_form"),
    
    
    path('view_all/', views.view_all_data, name='view_all_data'),
    path('view_detail/', views.view_data_detail, name='view_data_detail'),
    path('view_detail/feedback/<int:feedback_id>/', views.view_data_detail, name='view_feedback_detail'),
    path('view_detail/semic/<int:semic_form_id>/', views.view_data_detail, name='view_semic_detail'),
    # reminder
    
    path('create_event', create_event, name='create_event'),
]