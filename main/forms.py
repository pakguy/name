from django import forms
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.forms import UserChangeForm
from .models import Exam,  School,Semic_form,Feedback
from pytz import common_timezones

# class ContactusForm(forms.Form):
#     Name = forms.CharField(max_length=30)
#     Email = forms.EmailField()
#     Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


class ExamVenueForm(forms.ModelForm):
    class Meta:
        model=models.ExamVenue
        fields=['name','code']

class ExamHallForm(forms.ModelForm):
    class Meta:
        model=models.ExamHall
        fields=['name','venue','no_of_seats']
        
class Invigilator_AllocateForm(forms.ModelForm):
    class Meta:
        model=models.invigilator_allocate
        fields=['invigilator','hall']
        
class Student_AllocateForm(forms.ModelForm):
    class Meta:
        model=models.student_allocate
        fields=['student_allocated','hall']

class CourseForm(forms.ModelForm):
    class Meta:
        model=models.Course
        fields=['course_name','course_code','description','school','department','semester','level']

class AdminUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ["venue", "end_time", "start_time", "date", "type", "course"]


class UpdateAdminForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

class semicForm(forms.ModelForm):
    class Meta:
        model = Semic_form
        fields =["student_name","matric_no", "course_title", "course_code", "student_comment", "invigilator_comment", "semic_attachment"]
        
class Feedback_Form(forms.ModelForm):
    class Meta:
        model =Feedback
        fields =["course_title", "course_code", "specific_feedback", "suggestion_for_improvement", "feedback_attachment"]

class AdminConfigForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ["name"]

class EventForm(forms.Form):
    summary = forms.CharField(label='Summary', max_length=100)
    start_datetime = forms.DateTimeField(label='Start Date and Time', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'))
    end_datetime = forms.DateTimeField(label='End Date and Time', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'))
    location = forms.CharField(label='Location', max_length=100)
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(attrs={'placeholder': 'Course code:____\nCourse title:____\nDay:____\nDate:____\nExam Type:____\nStart time:____\nEnd time:____\nVenue:____'})
    )
    timezone = forms.ChoiceField(label='Timezone', choices=[(tz, tz) for tz in common_timezones])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.initial.get('description'):
            self.initial['description'] = (
                "Course code:\n"
                "Course title:\n"
                "Day:\n"
                "Date:\n"
                "Exam Type:\n"
                "Start time:\n"
                "End time:\n"
            )
            


            