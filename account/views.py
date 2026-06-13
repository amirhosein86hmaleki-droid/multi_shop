from django.shortcuts import render,redirect,reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser

from .serializers import UserSerializer
from .models import User, Otp
from .forms import LoginForm, RegisterForm, CheckOtpForm

from kavenegar import *
from random import randint
from django.utils.crypto import get_random_string
from uuid import uuid4
# Create your views here.

class UserView(APIView):
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, )
    def get(self, request):
        user = request.user
        serializer=UserSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request):
        user=request.user
        serializer = UserSerializer(data=request.data, instance=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                                        # ====API====
# ============================================================================================================

# def user_login(request):
#     return render(request, 'account/login.html', {})

class UserLogin(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})
    

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd= form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None :
                login(request, user)
                return redirect('/')
            
            else:
                form.add_error("phone","invalid user data")
        else:
            form.add_error("phone", "invalid data")
        
        return render(request, 'account/login.html', {'form': form})


# ******************************************************************************************
                                    # RegisterView
class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/otp_login.html', {'form':form})
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(1000, 9999)
            try:
                api = KavenegarAPI('6E59663678536F7949327A47772F707845504769386B54416C36575879486F54552B6F41365676682F35303D')
                params = {
                    'receptor': cd["phone"],
                    'template': 'login',
                    'token': randcode,
                    'type': 'sms',#sms vs call
                }   
                response = api.verify_lookup(params)
                print(response)
            except APIException as e: 
                print(e)
            except HTTPException as e: 
                print(e)
            token = str(uuid4())
            Otp.objects.update_or_create(phone=cd['phone'], defaults={
                'token': token,
                'code':randcode
            })
            print(randcode)
            return redirect(reverse('account:check_otp') + f'?token={token}')
        else:
            form.add_error('phone', 'invalid data')
        return render(request, 'account/otp_login.html', {'form':form})
# |========================================================================================================|
                                            #|CheckOtpView|

class CheckOtpView(View):
    def get(self, request):
        form=CheckOtpForm()
        return render(request, 'account/check_otp.html', {'form':form})

    def post(self, request):
        token = request.GET.get('token')
        form= CheckOtpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd['code'], token=token).exists():
                otp= Otp.objects.get(token=token)
                user, create = User.objects.update_or_create(phone=otp.phone)
                login(request, user)
                return redirect('/')
            
        else:

            form.add_error('code', 'invalid data')

        return render(request, 'account/check_otp.html', {'form':form})  

# |================================================================================================|

def user_logout(request):
    logout(request)
    return redirect('/')

