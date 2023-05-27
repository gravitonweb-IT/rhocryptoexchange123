
from django.urls import path
from .views import  *
# from account.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('register', UserRegistrationView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login'),
    path('uploadPaymentDetails', UploadPaymentDetails.as_view(), name='uploadPaymentDetails'),

    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)