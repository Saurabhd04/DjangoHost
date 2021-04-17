from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Register(AbstractUser):
    # FirstName = models.CharField(max_length=100)
    # MiddleName = models.CharField(max_length=100)
    # LastName = models.CharField(max_length=100)
    # UserName = models.CharField(max_length=50)
    # EmailId = models.EmailField(max_length=50)
    AadhaarRegisteredMobileNumber = models.BigIntegerField(null=True)
    AadhaarNumber = models.CharField(max_length=12, null = True)
    # Password = models.CharField(max_length=50)
    #ConfirmPassword = models.CharField(max_length=50)
    AlternateMobileNumber = models.BigIntegerField(null = True)
    # Otp = models.BooleanField()
    # Otp2 = models.BooleanField()

    def __str__(self):
        return self.email



    
