from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(StudentLevel)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Semic_form)
admin.site.register(Feedback)
admin.site.register(student_allocate)
admin.site.register(ExamVenue)
admin.site.register(ExamHall)
admin.site.register(invigilator_allocate)
admin.site.register(Exam)