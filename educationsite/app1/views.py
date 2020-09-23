
from django.shortcuts import render , redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from user.forms import UserRegisterForm ,contactform , reqform
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.core.paginator import PageNotAnInteger,Page, Paginator,EmptyPage
from time import gmtime, strftime
from datetime import datetime
import random
import string
from django.http import JsonResponse
from django.template.loader import render_to_string

# from django.utils.timezone import datetime



def home(request):
    
    courseHome = courses.objects.all()[:12]
    context = {
        'courses_' : courseHome
    }
    return render(request,'index.html', context)


def courseDesc(request,serial):
    courseDetail = courses.objects.filter(serialNo=serial)
    context = {
        'specs':courseDetail[0]
    }
    return render(request,'course_details.html',context)

def about(request):
    return render(request,'about.html')


def allCourses(request):
    bak = courses.objects.all()
    pag = Paginator(bak,20)
    pg = request.GET.get('page')
    try:
        jolly = pag.page(pg)
    except EmptyPage:
        jolly = pag.page(num_pages)
    except PageNotAnInteger:
        jolly = pag.page(1)

 
    context ={
        'ads':bak,
        'jolly':jolly,
        
    }
    return render(request,'courses.html',context)




def contactUs(request):
    return render(request,'contact.html')


def signUp(request):
    if request.method == 'POST':
        uEmail = request.POST.get('userEmail')
        uPass1 = request.POST.get('userPassword1')
        upass2 = request.POST.get('userPassword2')
       

        if uEmail and uPass1 and upass2:
            user_ = User.objects.create_user(uEmail, email=None, password=uPass1)
            # dual check
            userCheck = authenticate(username=uEmail, password=uPass1)
            if userCheck is not None:
                login(request, userCheck)
                return redirect('home')
        else:
            return render(request,'signUp.html',{'message': 'Quit Playing arround!!! Fields can not be blank any where on this site.'})
            
        

    
    else:
    # No backend authenticated the credentials
        return render(request,'signUp.html')

    



def signIn(request):
    uname = request.POST.get('loginEmail')
    upass = request.POST.get('loginPassword')
    if request.method == 'POST':
        user = authenticate(username=uname, password=upass)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('home')
        else:
        # No backend authenticated the credentials

            return render(request,'signin.html',{'message':'Login failed! Invalid credentials'})
    else:
            return render(request,'signin.html')



def logOut(request):
    logout(request)
    return redirect('home')




def nwCourse(request):
    return render(request,'nwCourse.html')




def tnc(request):
    return render(request,'tnc.html')



def verifyCertificate(request):

    

    try:
        serial = request.GET.get('serial')
        if serial != None:
            nt = certificateIssued.objects.filter(certificateSerial=serial)[0]
            return render(request,'certificateVerification.html',{'peter':nt})
        
    except:
        return render(request,'certificateVerification.html',{'peter':'None'})





def testPage(request):
    
    return render(request,'testPage.html')


def ajaxCheck(request):
    email = request.GET.get('email_')
    today = datetime.today()
    instance = successfullPayments.objects.filter(paymentEmail=email,paymentDate__year=today.year, paymentDate__month=today.month, paymentDate__day=today.day)
    if instance:
        courses__ = beforePaymentCourseDetails.objects.filter(userEmail=instance[0].paymentEmail,clickDate__year=today.year, clickDate__month=today.month, clickDate__day=today.day)
    jav = render_to_string(template_name="quizLinkpage.html",context={'pete':courses__})
    if instance:
        print("kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
        for a in range(0,20):
            print(jav)
    data = {'response':jav}
    
    return JsonResponse(data=data,safe=False)

@login_required
def paymentButton(request,email_,serial):
    instance = beforePaymentCourseDetails(userEmail=email_,courseSerial=serial)
    instance.save()
    return render(request,'paymentButton.html')



def hP4dP4EOMlFv4MzoyvhBn6fuqF7AeyGneyv9lIHCKuTAfE4h66CLUHO2zR5S(request):
    email_ = request.user.username
    instance = successfullPayments(paymentEmail=email_)
    instance.save()
    return render(request,'hP4dP4EOMlFv4MzoyvhBn6fuqF7AeyGneyv9lIHCKuTAfE4h66CLUHO2zR5S.html')



