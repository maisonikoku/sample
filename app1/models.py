from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=50,verbose_name='Enter Your Name')
    phone = models.IntegerField(help_text='phone number must be in 10 digits',verbose_name='Enter Phone Number')
    email = models.EmailField(verbose_name='Enter Mail Id')
    course = models.CharField(max_length=30,default="Others",choices=[('Java','Java'),('Python','Python'),('Full Stack','Full Stack'),('C','C'),("C++","C++"),("Others","Others")])

class Student(models.Model):
    stdId = models.CharField(max_length=10,verbose_name='Student Id')
    name = models.CharField(max_length=30)
    course = models.CharField(max_length=20,choices=[('Java','Java'),
                                                     ('Python','Python'),
                                                     ('C','C'),
                                                     ('C++','C++'),
                                                     ('Full Stack','Full Stack'),
                                                     ('Others','Others')])
    fees = models.IntegerField()
    phone = models.IntegerField()
    mail = models.EmailField()
    address = models.TextField(blank=True)

class Sample(models.Model):
    name = models.CharField(max_length=50)
