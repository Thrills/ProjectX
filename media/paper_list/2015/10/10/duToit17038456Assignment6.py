__author__ = '17038456@rga.stb.sun.ac.za'

#Tiaan du Toit 17038456
#SI ISM 354 Evaluation 6

from django.db import models #imports the models package from the django library

class Student(models.Model):
    student_no = models.IntegerField(length=7, primary_key=True) # Sets the unique primary key
    student_first_name = models.CharField(max_length=30) #
    student_last_name = models.CharField(max_length=30)
    student_date_of_birth = models.DateField('Birth Date')

class Subject(models.Model):
    subject_name = models.CharField(max_length=30)
    subject_code = models.IntegerField(max_length=10, primary_key=True)
    subject_faculty = models.CharField(max_length=30)
    subject_head = models.CharField(max_length=30)
    module = models.OneToOneField(Module) # Modules can only belong to one subject

class Module(models.Model):
    MODULE_TYPES = (
        ('S', 'Semester'),
        ('Y', 'Year')
    )
    module_type = models.Charfield(max_length=1, choices=MODULE_TYPES) # Module can either be year or semester
    module_lecturer_code = models.IntegerField(length=30)
    module_code = models.IntegerField(max_length=30, primary_key=True)
    module_name = models.CharField(max_length=30)
    module_mark = models.IntegerField(max_length=3) # marks is not a class,just an attribute
    subject = models.ForeignKey(Subject) # Subjects can have many modules
    student = models.ManyToManyField(Student) # Many students can take many modules and vice versa.




