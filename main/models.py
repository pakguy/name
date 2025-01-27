from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


class Semester(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
class StudentLevel(models.Model):
    name = models.CharField(max_length=5)
    
    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Department(models.Model):
    name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Course(models.Model):
    course_name = models.CharField(max_length=250)
    course_code = models.CharField(max_length=7, unique=True)
    description = models.TextField(blank=True, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    level = models.ForeignKey(StudentLevel, on_delete=models.CASCADE)
    class Meta:
        ordering = ['course_code']
        
    def __str__(self):
        return self.course_code + ' -> ' + self.course_name
    


# student models

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name=models.CharField(max_length=255, null=True)
    matric_no = models.CharField(max_length=15, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True)
    level = models.ForeignKey(StudentLevel, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL)
    profile_pic = models.ImageField(upload_to='Student/', null=True, blank=True)
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=14, null=False)
   
    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name
      
    def __str__(self):
        return self.get_name + " : " + self.user.username.replace(".", "/")
      
    def __str__(self):
        return f"{self.middle_name}  - {self.matric_no}"  



class Invigilator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    middle_name=models.CharField(max_length=255, null=True)
    profile_pic = models.ImageField(upload_to='Invigilator/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name
    @property
    def get_instance(self):
        return self
      
    def __str__(self):
        return self.user.first_name + " " +self.user.last_name

class Feedback(models.Model):
    course_title = models.CharField(max_length=255, null=True)
    course_code = models.CharField(max_length=15, null=True)
    specific_feedback = models.TextField(blank=True, null=True)
    suggestion_for_improvement =models.TextField(blank=True, null=True)
    feedback_attachment = models.FileField(upload_to='feedback/attachments/', null=True)
    
    def __str__(self):
        return f"{self.course_title} ({self.course_code}) - {self.feedback_attachment.name}"
    
class Semic_form(models.Model):
    student_name =models.CharField(max_length=255, null=True)
    matric_no =models.CharField(max_length=20, null=True)
    course_title =models.CharField(max_length=255, null=True)
    course_code =models.CharField(max_length=7,null=True)
    student_comment =models.TextField(blank=True, null=True)
    invigilator_comment =models.TextField(blank=True, null=True)
    semic_attachment = models.FileField(upload_to='semic/attachments')
    
    def __str__(self):
        return f"{self.student_name} - {self.course_code}"
    
class ExamVenue(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return f"{self.name} {self.code}"


class ExamHall(models.Model):
    name = models.CharField(max_length=20)
    venue = models.ForeignKey(ExamVenue, on_delete=models.CASCADE)
    no_of_seats = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} - {self.venue}- {self.no_of_seats}"
class invigilator_allocate(models.Model):
    invigilator = models.ForeignKey(Invigilator, on_delete=models.CASCADE, related_name='invigilator_allocations')
    hall =models.ForeignKey(ExamHall, on_delete=models.CASCADE, related_name='invigilator')
    def __str__(self):
        return f"{self.invigilator} {self.hall}"
    
class student_allocate(models.Model):
    student_allocated=models.ForeignKey(Student,on_delete=models.CASCADE, related_name='student_allocations')
    hall =models.ForeignKey(ExamHall, on_delete=models.CASCADE, related_name='student')
    def __str__(self):
        return f"{self.student_allocated} {self.hall}"

class Exam(models.Model):
    course = models.OneToOneField(Course, null=True, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=[('Paper Exam', 'Paper Exam'), ('CBT', 'CBT')], default='paper')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    venue = models.ForeignKey(ExamVenue, on_delete=models.SET_NULL, null=True, blank=True)
    # timetable = models.ForeignKey(ExamTimetable, on_delete=models.CASCADE)
    
    @property
    def get_day(self):
        days = [
          'monday',
          'tuesday',
          'wednesday',
          'thursday',
          'friday',
          'saturday',
          'sunday',
        ]
        return days[self.date.weekday()]
    
    @property
    def is_today(self):
        from datetime import date

        today = date.today()
        return self.date == today

    
    def __str__(self):
        return self.course.course_code + ' Exam'
    
