from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from main import models

# Create your views here.
# Create your views here.

# Create your views here.
def invigilator_signup_view(request):
    userForm=forms.InvigilatorUserForm()
    invigilatorForm=forms.InvigilatorForm()
    mydict={'userForm':userForm,'invigilatorForm':invigilatorForm}
    if request.method=='POST':
        userForm=forms.InvigilatorUserForm(request.POST)
        invigilatorForm=forms.InvigilatorForm(request.POST,request.FILES)
        if userForm.is_valid() and invigilatorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            invigilator=invigilatorForm.save(commit=False)
            invigilator.user=user
            invigilator.save()
            my_invigilator_group = Group.objects.get_or_create(name='INVIGILATOR')
            my_invigilator_group[0].user_set.add(user)
        return HttpResponseRedirect('login')
    return render(request,'invigilator/invigilatorsignup.html',context=mydict)


@user_passes_test(lambda u: u.is_superuser or u.groups.filter(name='INVIGILATOR').exists())
@login_required
def dashboard(request):
    Invigilator = models.Invigilator.objects.get(user=request.user,)
    
    context = {
        'invigilator': Invigilator,
    }
    return render(request, 'invigilator/invigilator_dashboard.html', context)
