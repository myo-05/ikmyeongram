from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage


# Create your views here.

"""
회원가입 페이지로 대체된 페이지 불러오는 임시 함수
정은 : 임시로 만들었습니다 + 영오: 기능구현해서 수정했습니다.
채연 : 위치바꿨습니다.
"""

# 회원가입
def sign_up(request):
    if request.method == "GET":  # 회원가입 페이지를 눌렀을 때
        return render(request, "user/signup.html")

    elif request.method == "POST":  # 회원가입정보 제출할 때
        username = request.POST.get("username", None)  # 회원 ID
        password = request.POST.get("password", None)  # 비밀번호
        password2 = request.POST.get("password2", None)  # 비밀번호 확인
        nickname = request.POST.get("nickname", None)  # 닉네임
        email = request.POST.get("email", None)  # 이메일       
        
        
        # 입력란이 모두 작성되어있다면 실행, 공란이 하나라도 있으면 else가 작동하여 에러메세지 출력
        if username and password and password2 and nickname and email:
            if password != password2:
                return render(
                    request,
                    "user/signup.html",
                    {"error_message": "[비밀번호불일치!] 진정하고 천천히 다시써봐요 예?"},
                )
            else:
                exist_user = get_user_model().objects.filter(username=username)
                if exist_user:
                    # 중복된 ID라면 회원가입창으로 돌아가기
                    # 영오: 이미 있는 ID입니다. 새로 지정해주세요. 메세지 떠야합니다.
                    return render(
                        request,
                        "user/signup.html",
                        {"error_message": "[중복 발견!] 이미 있는 ID입니다. 아시겠어요?"},
                    )
                else:
                    # 유저계정생성하여 DB저장
                    user=UserModel.objects.create_user(
                        username=username, #아이디
                        password=password, #비밀번호
                        nickname=nickname, #닉네임
                        email=email, #이메일
                    )
                    # 유저 이미지 불러와서 파일시스템에 저장하기
                    user_img = request.FILES.get("user_img",None) # 이미지 업로드 받아오기
                    
                    if user_img:
                        # 프로필사진 파일에 랜덤성 부여! → AWS 배포시 이름 겹치는 경우 고려
                        # user_img.name = 'user' + str(user.id) + '_' + str(
                        # random.randint(10000, 100000)) + '.' + str(user_img.name.split('.')[-1])
                        
                        # 파일을 시스템에 저장 | FileSystemStorage | DB가 아닌 시스템으로 지정한 dir에 저장
                        storage = FileSystemStorage()
                        # 
                        file_saved = storage.save(user_img.name, user_img)

                        # 저장한 파일의 경로를 url로 추출
                        uploaded_file_url = storage.url(file_saved)

                        # 신규 회원의 id 추출 후 업데이트
                        check = UserModel.objects.filter(id=user.id)
                        check.update(user_img=uploaded_file_url)
                # 회원가입 성공시 로그인 페이지로 이동
                return redirect("sign-in")
        # 공란이 하나라도 있으면 else가 작동하여 에러메세지 출력
        else:
            return render(
                request,
                "user/signup.html",
                {"error_message": "[빈칸 발견!] 공란이 빤히 보이는데, 미치셨어요?"},
            )


# 로그인 함수
def sign_in_view(request):
    if request.method == "POST":  # POST 요청, 즉 로그인을 시도했을 때
        username = request.POST.get("username", None)  # ID 받아옴
        password = request.POST.get("password", None)  # 비밀번호 받아옴

        user_check = auth.authenticate(request, username=username, password=password)  # 유저 인증(회원가입 된 유저인지)
        if user_check:  # 인증이 됐다면
            auth.login(request, user_check)
            return redirect("home")
        else:  # 인증이 안됐다면
            if UserModel.objects.filter(username=username).exists(): #아이디가 존재한다면
                return render(request, "user/signin.html", {"error_message" : "[비밀번호 오류!] 아...그거 그렇게 하는거 아닌뒈..!"})
            else:
                return render(request, "user/signin.html", {"error_message" : "[아이디 오류!] 뭐에오 가입하고 와요! 훠이훠이~!"})

    elif request.method == "GET":  # GET 요청, 즉 로그인페이지 버튼을 눌렀을 때
        user = request.user.is_authenticated
        if user:
            return redirect("home")
        else:
            return render(request, "user/signin.html")


# ============================= 로그아웃 ============================= 
@login_required
def logout(request):
    auth.logout(request)  # 인증 되어있는 정보를 없애기
    return redirect("home")


# ============================= 팔로우 ============================= 
def follow(request, user_id):
    if request.user.is_authenticated: # 로그인 된 경우에만
        target_user = UserModel.objects.get(id = user_id) # 팔로우할 유저의 정보를 가져온다.
        if target_user != request.user: # 현재 로그인한 유저와 타겟이 다를 경우(내가 아닌 경우)
            if target_user.followings.filter(id = request.user.id).exists(): # 이미 팔로우중인경우
                target_user.followings.remove(request.user) # 팔로우 삭제
            else: # 팔로우중이 아닌 경우
                target_user.followings.add(request.user) # 팔로우
        return redirect(request.META['HTTP_REFERER']) # 팔로우 완료하면 새로고침
    return redirect('sign-in') # 로그인이 되지 않은 경우 로그인 페이지로 넘어옴


# ============================= 팔로우, 팔로잉 리스트  ============================= 
def following_list(request, id):
    user = UserModel.objects.get(id=id)
    following_users = user.followers.all()
    return render(request, 'user/following_list.html', {'following_users': following_users})

def follower_list(request, id):
    user = UserModel.objects.get(id=id)
    follower_users = user.followings.all()
    return render(request, 'user/follower_list.html', {'follower_users': follower_users})