from django.shortcuts import render, redirect
from django.http import HttpResponse

from user.models import UserModel
from .models import Post
from django.contrib.auth.decorators import login_required


'''
[정은]
게시글 리스트 불러오기는 회원이랑 비회원 접근이 가능하기 때문에 바로 렌더 되게 해줬습니다!

[채연] 
정은님이 만드실 홈화면 구동을 위해 임시로 만들었습니다.
view 함수 이름만 다르고 완전히 같으니까, 참고해서 merge 해 주시면 됩니다. 팀장님 ^-^* 찡긋~!
'''

    
'''
로그인 여부에 따라 화면 넘어가는 함수 - 기존 home 함수에서 수정했습니다. 
로그인이 안 되어있을 땐 로그인 화면,
로그인이 되어있을 때는 홈 화면으로 넘어가되
홈에서 글 데이터베이스를 불러옵니다. html에서 이 리스트를 보여줍니다.
'''
def home(request):
    user = request.user.is_authenticated # 로그인 여부 검증
    if user: # 로그인 했으면 홈으로 넘어가기 # models의 Post 객체를 가져온다. (모든 글 가져오기)
        all_post = Post.objects.all().order_by('-created_at')
        return render(request, 'sns/home.html',{'posts':all_post})
    else:
        return redirect('sign-in')


def new(request): # 새 글 작성 페이지로 렌더링
    return render(request, 'sns/new_post.html')
    
    
# 글 작성
@login_required(login_url='/sign-in') # 로그인을 하지 않고 url을 통해 접속할 경우 리디렉션
def new_post_view(request):
    '''
    게시글 db 에 저장된 제목, 내용, 이미지, 작성 시간, 작성자를 불러옵니다.
    '''
    if request.method == 'POST':
        post_title = request.POST['post_title'] # 글 제목
        post_content = request.POST['post_content'] # 글 내용
        # post_author = UserModel.object.get(id = request.user.id)
        post_img = request.FILES.get('post_img') # 이미지 업로드 받아오기
        
        
        post = Post.objects.create(post_title=post_title, post_content=post_content,  post_img=post_img, post_author=request.user.nickname)
        post.save()
        
        return redirect('home')
    
    return render(request, 'new_post.html')
        

# 게시글 상세보기
def detail_post_view(request, id):
    a_post = Post.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'sns/detail_post.html', {'post': a_post})