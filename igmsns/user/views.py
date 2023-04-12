from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def sign_up_view(request):
    return render(request, 'user/signup.html')


def sign_in_view(request):
    return render(request, 'user/signin.html')


# 정은 : 임시로 만들었습니다
def sign_up_detail(request):
    return render(request, 'user/signup_detail.html')
    