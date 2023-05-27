from django.db import models

# Create your models here.



class SignupModel(models.Model):
    image = models.ImageField(upload_to ='upload/images',null=True,blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=150,null=False,blank=False)
    email = models.CharField(max_length=150,null=False,blank=False)
    password = models.CharField(max_length=25,null=False,blank=False)
    # zipcode = models.CharField(max_length=6,null=False,blank=False)
    adharCard=models.ImageField(upload_to ='upload/images',null=True,blank=True)
    PanCard=models.ImageField(upload_to ='upload/images',null=True,blank=True)

class PaymentDetails(models.Model):
    CryptPrice=models.CharField(max_length=150,null=False,blank=False)
    IndianPrice=models.CharField(max_length=150,null=False,blank=False)
    PayementScreenShot=models.ImageField(upload_to ='upload/images',null=True,blank=True)