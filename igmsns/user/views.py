from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

"""
회원가입 페이지로 대체된 페이지 불러오는 임시 함수
정은 : 임시로 만들었습니다 + 영오: 기능구현해서 수정했습니다.
채연 : 위치바꿨습니다.
"""


def sign_up_detail(request):
    if request.method == "GET":  # 회원가입 페이지를 눌렀을 때
        return render(request, "user/signup_detail.html")

    elif request.method == "POST":  # 회원가입정보 제출할 때
        username = request.POST.get("username", None)  # 회원 ID
        password = request.POST.get("password", None)  # 비밀번호
        password2 = request.POST.get("password2", None)  # 비밀번호 확인
        nickname = request.POST.get("nickname", None)  # 닉네임
        email = request.POST.get("email", None)  # 이메일
        user_img = request.FILES.get("user_img")  # 이미지 업로드 받아오기
        # 공란이 하나라도 있으면 else가 작동하여 에러메세지 출력
        if username and password and password2 and nickname and email:
            if password != password2:
                return render(
                    request,
                    "user/signup_detail.html",
                    {"error_message": "[비밀번호불일치!] 진정하고 천천히 다시써봐요 예?"},
                )
            else:
                exist_user = get_user_model().objects.filter(username=username)
                if exist_user:
                    # 중복된 ID라면 회원가입창으로 돌아가기
                    # 영오: 이미 있는 ID입니다. 새로 지정해주세요. 메세지 떠야합니다.
                    return render(
                        request,
                        "user/signup_detail.html",
                        {"error_message": "[중복 발견!] 이미 있는 ID입니다. 아시겠어요?"},
                    )
                else:
                    # 유저계정생성하여 DB저장
                    # 영오: 회원가입완료. 메세지 떠야합니다.
                    UserModel.objects.create_user(
                        username=username,
                        password=password,
                        nickname=nickname,
                        email=email,
                        user_img=user_img,
                    )
                    return redirect("sign-in")
        else:
            return render(
                request,
                "user/signup_detail.html",
                {"error_message": "[빈칸 발견!] 공란이 빤히 보이는데, 미치셨어요?"},
            )


# 로그인 함수
def sign_in_view(request):
    if request.method == "POST":  # POST 요청, 즉 로그인을 시도했을 때
        username = request.POST.get("username", None)  # ID 받아옴
        password = request.POST.get("password", None)  # 비밀번호 받아옴

        me = auth.authenticate(
            request, username=username, password=password
        )  # 유저 인증(회원가입 된 유저인지)
        if me is not None:  # 계정이 있다면
            auth.login(request, me)
            return redirect("home")
        else:  # 계정이 없다면
            return redirect("sign-in")

    elif request.method == "GET":  # GET 요청, 즉 로그인페이지 버튼을 눌렀을 때
        user = request.user.is_authenticated
        if user:
            return redirect("home")
        else:
            return render(request, "user/signin.html")


# 로그아웃
@login_required
def logout(request):
    auth.logout(request)  # 인증 되어있는 정보를 없애기
    return redirect("home")
