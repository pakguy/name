from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from main import models as QMODEL
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from main.models import Course, Student


# Create your views here.

def student_signup_view(request):
    userForm=forms.StudentUserForm()
    studentForm=forms.StudentForm()
    mydict={'userForm':userForm,'studentForm':studentForm}
    if request.method=='POST':
        userForm=forms.StudentUserForm(request.POST)
        studentForm=forms.StudentForm(request.POST,request.FILES)
        if userForm.is_valid() and studentForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            student=studentForm.save(commit=False)
            student.user=user
            student.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        return HttpResponseRedirect('login')
    return render(request,'student/studentsignup.html',context=mydict)


@login_required
def studentDashboard(request):
    student = Student.objects.get(user=request.user)

    if student.department:
        courses = Course.objects.filter(
            department=student.department, level=student.level
        ).values()
    else:
        courses = []

    context = {"courses": courses, "student": student}
    return render(request, "student/student_dashboard.html", context)

@login_required
def studentProfile(request):
    student = Student.objects.get(user=request.user)
    return render(request, "student/student_profile.html", { "student": student})
