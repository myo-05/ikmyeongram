from django.shortcuts import render, redirect
from .models import Post


# Create your views here.

'''
정은님이 만드실 홈화면 구동을 위해 임시로 만들었습니다 뷰 함수 이름만 다르고 완전히 같으니까 참고해서 merge 해 주시면 됩니다 팀장님 ^-^
'''
def home(request): # 홈 화면으로 렌더링
    all_post = Post.objects.all() # models의 Post 객체를 가져온다. (모든 글 가져오기)
    '''
    일단은 object.all로 했습니다. 어차피 제목만 넣을거긴 한데 그건 html템플릿에서 해주는게 나을것 같음(for)
    '''
    return render(request, 'sns/home.html',{'posts':all_post})
    

def new(request): # 새 글 작성 페이지로 렌더링
    return render(request, 'sns/new_post.html')
    
# @login_required(login_url='/sign-in') # 로그인을 하지 않고 url을 통해 접속할 경우 리디렉션
def new_post_view(request):
    if request.method == 'POST':
        post_title = request.POST['post_title']
        post_content = request.POST['post_content']
        # post_author = 유저id
        post = Post.objects.create(post_title=post_title, post_content=post_content)
        post.save()
        return redirect('home')
    return render(request, 'new_post.html')
        
        
        
        