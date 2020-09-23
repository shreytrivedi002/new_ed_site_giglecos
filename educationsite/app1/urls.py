from django.contrib import admin
from django.conf import settings
from django.urls import path , include
from . import views 
from django.conf.urls.static import static




urlpatterns = [

    path('', views.home , name='home' ),
    path('about/', views.about , name='about' ),
    # to indiv course
    path('courseDesc/<serial>', views.courseDesc , name='courseDesc' ),
    path('allCourses/courseDesc/<serial>', views.courseDesc , name='fromAllToCourseDesc' ),


    path('allCourses/', views.allCourses , name='allCourses' ),


    path('nwCourse/', views.nwCourse , name='nwCourse' ),


# landing page right after  successful payment
    path('hP4dP4EOMlFv4MzoyvhBn6fuqF7AeyGneyv9lIHCKuTAfE4h66CLUHO2zR5S/', views.hP4dP4EOMlFv4MzoyvhBn6fuqF7AeyGneyv9lIHCKuTAfE4h66CLUHO2zR5S , name='hP4dP4EOMlFv4MzoyvhBn6fuqF7AeyGneyv9lIHCKuTAfE4h66CLUHO2zR5S' ),


    # page for test page after payment
    path('testPage/', views.testPage , name='testPage' ),
    path('ajaxCheck/', views.ajaxCheck , name='ajaxCheck' ),
    # payment button 
    path('courseDesc/paymentButton/<email_>/<serial>', views.paymentButton , name='paymentButton' ),
    path('allCourses/courseDesc/paymentButton/<email_>/<serial>', views.paymentButton , name='paymentButton' ),



    

    path('tnc/', views.tnc , name='tnc' ),
    path('verifyCertificate/', views.verifyCertificate , name='verifyCertificate' ),



    path('contactUs/', views.contactUs , name='contactUs' ),
    path('signIn/', views.signIn , name='signIn' ),
    path('logOut/', views.logOut , name='logOut' ),
    path('signUp/', views.signUp , name='signUp' ),









    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)