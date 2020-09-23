from django.db import models
from django.contrib.auth.models import User




class courses(models.Model):
    addToPopular = models.BooleanField(default=False)
    link1 = models.CharField(max_length=250,default=0)
    link2 = models.CharField(max_length=250,default=0)
    link3 = models.CharField(max_length=250,default=0)
    link4 = models.CharField(max_length=250,default=0)
    link5 = models.CharField(max_length=250,default=0)
    link6 = models.CharField(max_length=250,default=0)
    courseTitle = models.CharField( max_length=250,default=0)
    courseDesc = models.CharField( max_length=450,blank=True)
    priceAfterDiscount = models.CharField( max_length=10,default=0)
    courseRating = models.IntegerField(default='0')
    priceBeforeDiscount = models.CharField( max_length=10,default=0)
    serialNo = models.CharField( max_length=50,default=0)
    testFormUrl = models.URLField( max_length=1000,default=0)
    


    def __str__(self):
        return self.courseTitle




class certificateIssued(models.Model):
    certificateSerial = models.CharField(max_length=10)
    name = models.CharField( max_length=50)
    courseName = models.CharField( max_length=150)
    dateIssued = models.DateTimeField()

    def __str__(self):
        return self.name + '|||' + str(self.dateIssued)  + '|||'  +  self.courseName





class successfullPayments(models.Model):
    paymentEmail = models.CharField( max_length=50)
    paymentDate = models.DateTimeField( auto_now_add=True,null=True)

    def __str__(self):
        return self.paymentEmail + '|||' + str(self.paymentDate)



class beforePaymentCourseDetails(models.Model):
    userEmail = models.CharField( max_length=50)
    courseSerial = models.CharField( max_length=50)
    clickDate = models.DateTimeField( auto_now_add=True,null=True)

    def __str__(self):
        return self.userEmail + '|||' + str(self.clickDate)