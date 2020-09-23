from django import template
from app1.models import *
from time import gmtime, strftime
from datetime import datetime
# from datetime import date
from django.contrib.auth.models import User


register = template.Library()

today =  datetime.today()

@register.simple_tag
def courseCount():
    no = courses.objects.all().count()
    return no
   


@register.simple_tag
def allCourses():
    no = courses.objects.all()
    return no
   

@register.simple_tag
def allCourseSerial(a):
    serialNumber = beforePaymentCourseDetails.objects.filter(userEmail=a,clickDate__year=today.year, clickDate__month=today.month, clickDate__day=today.day)
    return serialNumber
   



@register.simple_tag
def getQuizLink(a):
    quizlink = courses.objects.filter(serialNo=a).only('courseTitle','testFormUrl')[0]
    return quizlink
   


   

@register.simple_tag
def totalCertificates():
    count = certificateIssued.objects.all().count()
    count = count + 100
    return count
   