from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.

#회원가입 함수
def sign_up_view(request):
    if request.method == 'GET': #회원가입 페이지를 눌렀을 때
        return render(request, 'user/signup.html')
    
    elif request.method == 'POST': #회원가입정보 제출할 때
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        # remove 'bio'
        nickname = request.POST.get('nickname', None)

        if password != password2:
            return render(request, 'user/signup.html')
        else:
            exist_user = get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html')
            else:
                UserModel.objects.create_user(
                    username=username, password=password, nickname = nickname)
                return redirect('sign-in')

#로그인 함수
def sign_in_view(request):
    if request.method == 'POST': #POST 요청, 즉 로그인을 시도했을 때
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)
        if me is not None: #계정이 있다면
            auth.login(request, me)
            return redirect('home')
        else:
            return redirect('sign-in')

    elif request.method == 'GET': #GET 요청, 즉 로그인페이지 버튼을 눌렀을 때
        user = request.user.is_authenticated
        if user:
            return redirect('home')
        else:
            return render(request, 'user/signin.html')


#회원가입 페이지로 대체된 페이지 불러오는 임시 함수
# 정은 : 임시로 만들었습니다
def sign_up_detail(request):
    return render(request, 'user/signup_detail.html')



# 로그아웃
@login_required
def logout(request):
    auth.logout(request) # 인증 되어있는 정보를 없애기
    return redirect("home")