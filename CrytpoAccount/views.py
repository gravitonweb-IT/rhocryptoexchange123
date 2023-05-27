from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from django.http import HttpResponse
from .models import *
import json
class UserRegistrationView(APIView):
  def post(self, request, format=None):
      Data = request.data
      print(Data)
      s=SignupModel.objects.create(image=request.data.get("image"),name=request.data.get("name"),email=request.data.get("email"),password=request.data.get("password"),adharCard=request.data.get("adharCard"),PanCard=request.data.get("PanCard"))
      s.save()
      finalObj={}
      finalObj["email"]=request.data.get("email")
      finalObj["name"]=request.data.get("name")
      # data = serializers.serialize('json', LastLogin.objects.filter(userlogin_id=user1))
      return HttpResponse(json.dumps(finalObj),content_type='application/json')    
from django.core import serializers
class UserLoginView(APIView):
  def post(self, request, format=None):
      Data = request.data
      print(Data)
      s=SignupModel.objects.filter(email=request.data.get("email"),password=request.data.get("password"))
      data = serializers.serialize('json', s)
      print(s)
      # data = serializers.serialize('json', LastLogin.objects.filter(userlogin_id=user1))
      return HttpResponse(data,content_type='application/json') 

class UploadPaymentDetails(APIView):
  def post(self, request, format=None):
      Data = request.data
      print(Data)
      s=PaymentDetails.objects.create(CryptPrice=request.data.get("CryptPrice"),IndianPrice=request.data.get("IndianPrice"),PayementScreenShot=request.data.get("PayementScreenShot"))
      s.save()
      # data = serializers.serialize('json', LastLogin.objects.filter(userlogin_id=user1))
      return HttpResponse("success",content_type='application/json')   