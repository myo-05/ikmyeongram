from django.shortcuts import render, redirect
from django.http import HttpResponse

from user.models import UserModel
from .models import Post
from user.models import UserModel
from django.contrib.auth.decorators import login_required


'''
[정은]
게시글 리스트 불러오기는 회원이랑 비회원 접근이 가능하기 때문에 바로 렌더 되게 해줬습니다!

[채연] 
정은님이 만드실 홈화면 구동을 위해 임시로 만들었습니다.
view 함수 이름만 다르고 완전히 같으니까, 참고해서 merge 해 주시면 됩니다. 팀장님 ^-^* 찡긋~!
'''

# 홈이동 (피드페이지)
# 로그인 없이도 피드는 조회가능하지만, 글작성버튼은 없다.
def home(request):
    all_post = Post.objects.all().order_by('-created_at') #모든 글을 가져와 생성일 기준으로 내림차순나열
    return render(request, 'sns/home.html',{'posts':all_post})


def new(request): # 새 글 작성 페이지로 렌더링
    return render(request, 'sns/new_post.html')
    
    
# 글 작성
@login_required(login_url='/sign-in') # 로그인을 하지 않고 url을 통해 접속할 경우 리디렉션
def new_post_view(request):
    '''
    제목, 내용, 이미지, 작성 시간, 작성자를 게시글 db 에 저장합니다.
    '''
    if request.method == 'POST':
        post_title = request.POST['post_title'] # 입력한 글 제목 받아오기
        post_content = request.POST['post_content'] # 입력한 글 내용 받아오기
        post_author = request.user.nickname #현재 로그인된 user의 nickname을 받아오기
        post_img = request.FILES.get('post_img') # 이미지 업로드 받아오기
        
        post = Post.objects.create(post_title=post_title, post_content=post_content, post_img=post_img, post_author= post_author)
        post.save()
        
        return redirect('home')
    
    return render(request, 'new_post.html')
        

# 게시글 상세보기
def detail_post_view(request, id):
    a_post = Post.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'sns/detail_post.html', {'post': a_post})


# 게시글 삭제
@login_required(login_url='/sign-in') # 로그인을 하지 않고 url을 통해 접속할 경우 리디렉션
def delete(request, id):
    Post.objects.get(id=id).delete()
    return redirect('home') #삭제 성공!


#게시글 수정하기
@login_required(login_url='/sign-in') # 로그인을 하지 않고 url을 통해 접속할 경우 리디렉션
def update(request,id ):   
    post = Post.objects.get(id=id) 
    if request.method == 'POST':
        post_title = request.POST['post_title'] #수정할 제목 받아오기
        post_content = request.POST['post_content'] #수정할 내용 받아오기
        post_author = request.user.id #현재 로그인된 user의 id를 받아오기
        post_img = request.FILES.get('post_img') # 이미지 업로드 받아오기
        # update_at = request.datetie

        post = Post.objects.update(id=id,post_title=post_title, post_content=post_content, post_img=post_img,post_author=post_author)


        return redirect('home')
    else: # GET
        
        return render(request, 'sns/new_update.html', {'post': post})
            
    
# 프로필 페이지보기 + 해당함수를 실행할 버튼을 고려해야합니다. + 버튼을 누르면 특정 user의 id를 불러와야합니다.
@login_required(login_url='/sign-in') # 로그인을 하지 않고 url을 통해 접속할 경우 리디렉션
def profile_view(request, post_author):
    #특정 user의 id를 파라미터 id로 받아왔다면
    user = UserModel.objects.get(nickname=post_author) #user의 정보를 가져옴 -> 프로필사진 등 활용
    all_post = Post.objects.filter(post_author=post_author).order_by('-created_at') #user의 모든 글을 가져와서 생성일 기준으로 내림차순나열
    if request.method == 'GET':
        return render(request, 'sns/profile.html', {'user': user , 'posts': all_post})