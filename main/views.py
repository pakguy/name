from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User, auth

from django.contrib.auth.models import Group
from .forms import *
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required

from django.conf import settings
from datetime import date, timedelta
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from .forms import EventForm
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from django.core.exceptions import ValidationError
from django import forms
import logging
# Create your views here.

def is_invigilator(user):
    return user.groups.filter(name='INVIGILATOR').exists()

def is_student(user):
    return user.groups.filter(name='STUDENT').exists()



@login_required
def afterlogin_view(request):
    if request.user.is_superuser:
        return redirect('home')
    elif is_student(request.user):      
        return redirect('student/student-dashboard')
    elif is_invigilator(request.user):
        return redirect('invigilator/invigilator-dashboard')
def home(request):
    userId = request.user.id
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('examhalls')
        elif request.user.groups.filter(name="INVIGILATOR").exists():
            return redirect('examhalls')
        elif User.objects.filter(pk=userId, groups__name='STUDENT').exists():
            print('Student')
            return redirect('student-dashboard')
    
    return render(request, "login.html")


@login_required
@staff_member_required
def view_all_data(request):
    feedbacks = Feedback.objects.all()
    semic_forms = Semic_form.objects.all()
    context = {
        'feedbacks': feedbacks,
        'semic_forms': semic_forms
    }
    return render(request, 'view_all_data.html', context)

def view_data_detail(request, feedback_id=None, semic_form_id=None):
    feedback = get_object_or_404(Feedback, id=feedback_id) if feedback_id else None
    semic_form = get_object_or_404(Semic_form, id=semic_form_id) if semic_form_id else None
    context = {
        'feedback': feedback,
        'semic_form': semic_form
    }
    return render(request, 'view_data_detail.html', context)





def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method =="POST":
        username =request.POST["username"]
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html' )
    
    
def signup(request):
    return render(request, 'signup.html')




@staff_member_required
def assign_invigilator(request):
    invigilator_AllocatedForm=Invigilator_AllocateForm()
    if request.method=='POST':
        invigilator_AllocatedForm=Invigilator_AllocateForm(request.POST)
        if invigilator_AllocatedForm.is_valid():        
            invigilator_AllocatedForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/')
    return render(request,'assign_invigilator.html',{'invigilator_AllocatedForm':invigilator_AllocatedForm})




@login_required
@staff_member_required
def remove_invigilator(request,pk):
    invigilator=models.invigilator_allocate.objects.get(id=pk)
    invigilator.delete()
    return HttpResponseRedirect('/admin-view-invigilator-allocted')

# courses views
    
@login_required
@staff_member_required
def admin_add_course_view(request):
    courseForm=CourseForm()
    if request.method =='POST':
        courseForm=CourseForm(request.POST)
        if courseForm.is_valid():        
            courseForm=courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect(reverse('/admin-view-course'))
    return render(request,'admin_add_course.html',{'courseForm':courseForm})


@login_required
@staff_member_required
def admin_add_course_view(request):
    courseForm=CourseForm()
    if request.method=='POST':
        courseForm=CourseForm(request.POST)
        if courseForm.is_valid():        
            courseForm=courseForm.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('/admin-view-course')
    return render(request,'admin_add_course.html',{'courseForm':courseForm})


@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='INVIGILATOR').exists())
@login_required
def admin_view_course_view(request):
    courses = models.Course.objects.all()
    context ={'courses':courses}
    if request.user.groups.filter(name='INVIGILATOR').exists():
        # User is an invigilator
        return render(request,'invigilator/courses.html',context)
    else:
        # User is an admin
        return render(request,'admin_view_course.html',context)
    

@login_required
@staff_member_required
def delete_course_view(request,pk):
    course=models.Course.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/admin-view-course')

@login_required
@staff_member_required
def admin_course_view(request):
    return render(request,'admin_course.html')

# schedule views

@login_required
@staff_member_required
def adminScheduleEdit_by_item(request, pk):
    exam = Exam.objects.get(id=pk)
    examForm = ExamForm(instance=exam)
    if request.method == "POST":
        examForm = ExamForm(request.POST, instance=exam)
        if examForm.is_valid():
            examForm.save()
            return HttpResponseRedirect(reverse("admin_timetable"))

    context = {"examForm": examForm}
    return render(request, "edit_schedule.html", context)

@login_required
@staff_member_required
def deleteSchedule(request, pk):
    exam = Exam.objects.get(id=pk)

    if request.method == "POST":
        exam.delete()
        return redirect("admin-schedule-edit")

    context = {"exam": exam}
    return render(request, "delete-schedule.html", context)
@login_required
@staff_member_required
def deleteSchedule(request,pk):
    course=models.Exam.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect('/admin_timetable')


@login_required
@staff_member_required
def admin_add_exam(request):
    examform=ExamForm()
    if request.method=='POST':
        examform=ExamForm(request.POST)
        if examform.is_valid():        
            examform=examform.save()
            return HttpResponseRedirect('admin_timetable')
        else:
            print("form is invalid")
            print(examform.errors)
    return render(request,'admin_AddTimetable.html',{'examform': examform})

@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='INVIGILATOR').exists())
@login_required
def Semicform(request):
    semicform=semicForm()
    if request.method == "POST":
        semicform = semicForm(request.POST,  request.FILES)
        if semicform.is_valid():
            semicform=semicform.save()
            return HttpResponseRedirect('/')
        else:
            print("form is invalid")
    context ={
        'semicform':semicform
        }
    if request.user.groups.filter(name='INVIGILATOR').exists():
        # User is an invigilator
        return render(request,'invigilator/semicform.html',context)
    else:
        # User is an admin
        return render(request,'semicform.html',context)

def feedback_form(request):
    feedbackform = Feedback_Form()
    if request.method == "POST":
        feedbackform = Feedback_Form(request.POST, request.FILES)
        if feedbackform.is_valid():
            feedbackform=feedbackform.save()
            return HttpResponseRedirect('/')
        else:
            print("form is invalid")
    context ={
        'feedbackform': feedbackform
    }
    if request.user.groups.filter(name='STUDENT').exists():
        # User is a student
        return render(request, 'student/feedbackform.html', context)
    elif request.user.groups.filter(name='INVIGILATOR').exists():
        # User is an invigilator
        return render(request, 'invigilator/feedbackform.html', context)
    else:
        return render(request, 'feedbackform.html', context)
    


@login_required
def admin_timetable(request):
    exam = models.Exam.objects.all()
    department = models.School.objects.all()

    if request.user.groups.filter(name='STUDENT').exists():
        # User is a student
        context = {'department': department, 'exam': exam}
        return render(request, 'student/timetable.html', context)
    elif request.user.groups.filter(name='INVIGILATOR').exists():
        # User is an invigilator
        context = {'department': department, 'exam': exam}
        return render(request, 'invigilator/timetable.html', context)
    else:
        # Default case, handle as needed
        context = {'department': department, 'exam': exam}
        return render(request, 'admin_timetable.html', context)



@login_required
@staff_member_required
def adminProfile(request):
    if not (request.user.is_staff):
        return redirect("home")
    userForm = AdminUserForm(instance=request.user)

    if request.method == "POST":
        userForm = AdminUserForm(request.POST, instance=request.user)
        if userForm.is_valid():
            userForm.save()
            return redirect("/")
        else:
            messages.error(request, "Sorry, an error occured.")

    context = {"userForm": userForm, "userForm_errors": userForm.errors}
    return render(request, "admin-profile.html", context)


@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='INVIGILATOR').exists())
@login_required
def your_view(request):
    exam_rooms = models.ExamHall.objects.all()
    
    context = {
        'exam_rooms': exam_rooms,
    }
    if request.user.groups.filter(name='INVIGILATOR').exists():
        # User is an invigilator
        return render(request, 'invigilator/examhalls.html', context)
    else:
        # User is an admin
        return render(request, 'admin_examhalls.html', context)
    

@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='INVIGILATOR').exists())
@login_required
def view_examroom_details(request, examroom_id):
    examroom = models.ExamHall.objects.get(pk=examroom_id)
    invigilators = models.Invigilator.objects.filter(pk=examroom_id)
    student =models.Student.objects.filter(pk=examroom_id)
    context ={
        'examroom': examroom,
        'student':student,
        'invigilators': invigilators,
    }
    if request.user.groups.filter(name='INVIGILATOR').exists():
        # User is an invigilator
        return render(request, 'invigilator/examhall_details.html', context)
    else:
        # User is an admin
        return render(request,'examhall_details.html', context)
    
 
# reminder views

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def get_credentials():
    creed = None
    if os.path.exists(r"C:\Users\Public\download\token.json"):
        creed = Credentials.from_authorized_user_file(r"C:\Users\Public\\download\token.json")
    if not creed or not creed.valid:
        if creed and creed.expired and creed.refresh_token:
            creed.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_config( {
                "installed": {
                    "client_id": "959485250535-321th3rlu04o5g8d8bbbabhv1091n4j9.apps.googleusercontent.com",
                    "project_id": "warm-physics-421107",
                    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                    "token_uri": "https://oauth2.googleapis.com/token",
                    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                    "client_secret": "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",
                    "redirect_uris": ["http://localhost"]
                }
            },
            SCOPES
        )
           
            creed = flow.run_local_server(port=0)
        with open(r"C:\Users\Public\token.json", "w") as token:
            token.write(creed.to_json())
    return creed
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            start_datetime = form.cleaned_data['start_datetime']
            end_datetime = form.cleaned_data['end_datetime']
            
            if start_datetime >= end_datetime:
                form.add_error('end_datetime', 'End time must be after start time.')
                return render(request, 'create_event.html', {'form': form})
            
            try:
                creed = get_credentials()
                service = build("calendar", "v3", credentials=creed)

                summary = form.cleaned_data['summary']
                location = form.cleaned_data['location']
                description = form.cleaned_data['description']
                start_datetime_str = start_datetime.strftime('%Y-%m-%dT%H:%M:%S%z')
                end_datetime_str = end_datetime.strftime('%Y-%m-%dT%H:%M:%S%z')
                timezone = form.cleaned_data['timezone']

                event = {
                    "summary": summary,
                    "location": location,
                    "description": description,
                    "start": {"dateTime": start_datetime_str, "timeZone": timezone},
                    "end": {"dateTime": end_datetime_str, "timeZone": timezone}
                }

                created_event = service.events().insert(calendarId="primary", body=event).execute()
                message = f"Event created: {created_event.get('htmlLink')}"
                return render(request, 'success_template.html', {'message': message})
            except HttpError as error:
                logging.error("An error occurred while creating the event: %s", error)
                return HttpResponse("An error occurred while creating the event. Please try again later.")
            except Exception as e:
                logging.exception("Unexpected error occurred: %s", e)
                return HttpResponse("An unexpected error occurred. Please contact the administrator.")
    else:
        form = EventForm()
    exam = models.Exam.objects.all()
    department = models.School.objects.all()
    context = {'department': department, 'exam': exam, 'form': form}
    if request.user.groups.filter(name='STUDENT').exists():
        # User is a student
        context = {'department': department, 'exam': exam, 'form': form}
        return render(request, 'student/create_event.html', context)
    elif request.user.groups.filter(name='INVIGILATOR').exists():
        # User is an invigilator
        context = {'department': department, 'exam': exam, 'form': form}
        return render(request, 'invigilator/invigilator_create_event.html', context)
    else:
        # Default case, handle as needed
        context = {'department': department, 'exam': exam, 'form': form}
        return render(request, 'create_event.html', context)
    
    
def main():
    creed =get_credentials()
    service = build("calendar","v3", credentials=creed)
    create_event(service)


