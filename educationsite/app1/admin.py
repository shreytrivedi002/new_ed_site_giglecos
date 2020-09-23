from django.contrib import admin
from .models import *


admin.site.register(courses)
admin.site.register(certificateIssued)
admin.site.register(successfullPayments)
admin.site.register(beforePaymentCourseDetails)

