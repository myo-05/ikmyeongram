from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Comment, Post
from user.models import UserModel
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST


'''
[정은]
게시글 리스트 불러오기는 회원이랑 비회원 접근이 가능하기 때문에 바로 렌더 되게 해줬습니다!

[채연] 
정은님이 만드실 홈화면 구동을 위해 임시로 만들었습니다.
view 함수 이름만 다르고 완전히 같으니까, 참고해서 merge 해 주시면 됩니다. 팀장님 ^-^* 찡긋~!
'''

# ============================= 홈이동 (피드페이지) ============================= 

# 로그인 없이도 피드는 조회가능하지만, 글작성버튼은 없다.
def home(request):
    all_post = Post.objects.all().order_by('-created_at') #모든 글을 가져와 생성일 기준으로 내림차순나열
    return render(request, 'sns/home.html',{'posts':all_post})


def new(request): # 새 글 작성 페이지로 렌더링
    return render(request, 'sns/new_post.html')
    
    
#  ============================= 글 작성 ============================= 

def new_post_view(request):
    '''
    제목, 내용, 이미지, 작성 시간, 작성자를 게시글 db 에 저장합니다.
    '''
    if request.user.is_authenticated: # 로그인 인증 여부
        
        if request.method == 'POST':
            post_title = request.POST['post_title'] # 입력한 글 제목 받아오기
            post_content = request.POST['post_content'] # 입력한 글 내용 받아오기
            post_author = request.user #현재 로그인된 user의 nickname을 받아오기 (외래키 연결됨)
            post_img = request.FILES.get('post_img') # 이미지 업로드 받아오기
            post_author_id = request.user.id
            
            post = Post.objects.create(post_title=post_title, post_content=post_content, post_img=post_img, post_author= post_author, author_id = post_author_id)
            post.save()
            
            return redirect('home')
        
        return render(request, 'new_post.html')
    
    return redirect('sign-in')    

# ============================= 게시글 상세보기 ============================= 

def detail_post_view(request, id):
    a_post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=a_post).order_by('-created_at')
    if request.method == 'GET':
        return render(request, 'sns/detail_post.html', {'post': a_post, 'comments':comments})

'''
수정 뷰, 삭제 뷰 위치 바꿨습니다. 기능의 흐름에 따라 함수를 배치하는 게 알아보기 쉬울 것 같습니다.
'''

# ============================= 게시글 수정하기 ============================= 

def update(request,id ):   
    a_post = Post.objects.get(id=id) 
    comments = Comment.objects.filter(post=a_post).order_by('-created_at')
    if request.method == 'POST':
        if a_post.post_author == request.user:  # 현재 로그인된 사용자가 게시글 작성자인 경우에만 수정 가능
            a_post.post_title = request.POST['post_title'] # 수정할 제목 받아오기
            a_post.post_content = request.POST['post_content'] # 수정할 내용 받아오기
            #post.post_author = request.user.id # 현재 로그인된 user의 id를 받아오기 나중에 내 글만 수정 가능하게 할 때 사용
            a_post.post_img = request.FILES.get('post_img') or a_post.post_img
            # 이미지 업로드 받아오기, 이미지를 새로 업로드하지 않는다면 기존 이미지를 그대로 사용한다.
            a_post.save()
            '''
            post = Post.objects.update(post_title=post_title, post_content=post_content, post_img=post_img,post_author=post_author)
            update 를 하면 테이블 내의 모든 속성들이 업데이트 됩니다.
            id = id 라고 하면 모든 id 어트리뷰트가 같은 값으로 업데이트 되어 UNIQE가 위배되어 오류가 나는 겁니다.
            그리고 id = id 를 삭제하게 되면 현재 목록의 모든 글이 같은 글이 됩니다.
            업데이트 시에도 save 사용해야 하니까 수정했습니다.
            수정 시간 반영 완료~
            '''
            return render(request, 'sns/detail_post.html', {'post': a_post, 'comments':comments})
        else:
            return HttpResponse("권한이 없습니다.") # 임시로 해뒀습니다. 경고창으로 바꿔야 합니다
    else:
        if a_post.post_author == request.user:  # 현재 로그인된 사용자가 게시글 작성자인 경우에만 수정 가능
            return render(request, 'sns/update_post.html', {'post': a_post})
            # 글 수정 html 파일 이름 수정 후 이 부분도 수정 완료 (new_update.html --> update_post.html)
        else:
            return HttpResponse("권한이 없습니다.") # 임시로 해뒀습니다. 경고창으로 바꿔야 합니다
        

# ============================= 게시글 삭제 ============================= 

def delete(request, id):
    post = Post.objects.get(id=id)
    if post.post_author == request.user:  # 현재 로그인된 사용자가 게시글 작성자인 경우에만 삭제 가능
        '''
        참고로 모든 로그인 사용자와 게시글 작성자 비교 구문은
        사용자가 해당 동작 url을 입력해 강제 이동해도 적용됩니다.
        '''
        post.delete()
        return redirect('home') # 삭제 성공
    else:
        return HttpResponse("권한이 없습니다.") # 임시로 해뒀습니다. 경고창으로 바꿔야 합니다

    
# ============================= 프로필 페이지보기  ============================= 

'''
로그인하지 않아도 보인다!
상세페이지에서 작성자의 이름을 클릭하면 이동
로그인 된 상태에서 헤더의 프로필 클릭시 이동
'''
def profile_view(request, author_id):
    #특정 user의 id를 파라미터 id로 받아왔다면
    user = UserModel.objects.get(id=author_id) #user의 정보를 가져옴 -> 프로필사진 등 활용
    all_post = Post.objects.filter(author_id=author_id).order_by('-created_at') #user의 모든 글을 가져와서 생성일 기준으로 내림차순나열
    total_post = all_post.count() #user의 작성글 갯수
    if request.method == 'GET':
        return render(request, 'sns/profile.html', {'total_post':total_post,'user': user , 'posts': all_post})
    
    
# ============================= 댓글 작성 =============================     

def comment_create(request,id):
    if request.user.is_authenticated: # 로그인 인증 여부
        post = Post.objects.get(id=id) # id값으로 해당 게시글을 찾아온다.
        if request.method == 'POST':
            comment = request.POST.get('comment', '') # 폼에서 댓글을 받아옴
            if comment == '': # 댓글이 없을 경우
                return HttpResponse('댓글을 입력해주세요.')
            else:
                Comment.objects.create(name= request.user.nickname, comment=comment, user=request.user, post=post) # 댓글을 db에 저장
                return redirect('detail', post.id) 
    return redirect('sign-in')       



# ============================= 댓글 수정 =============================

def comment_edit(request, id, comment_id):
    post = Post.objects.get(id=id)
    comment = Comment.objects.get(id=comment_id)

    if id == post.id and comment_id == comment.id:
        
        if request.method == 'POST':
            if comment.user == request.user:
                comment.comment = request.POST['comment']
                comment.save()
            return redirect('detail', id=post.id)

        context = {
            'post': post,
            'comment': comment,
            'edit_comment': comment.id,
            'comments': post.comment_set.all(),
        }
        return render(request, 'sns/detail_post.html', context)
    else:
        return HttpResponse("권한이 없습니다.")

# ============================= 댓글 삭제  ============================= 
def comment_delete(request, comment_id, id):
    comment = Comment.objects.get(id=comment_id)
    a_post = Post.objects.get(id=id)

    if id==a_post.id and comment_id==comment.id:  # 현재 로그인된 사용자가 게시글 작성자인 경우에만 삭제 가능
        comment.delete()
        return redirect('detail', id=a_post.id) # 삭제 성공 후 상세 페이지로 이동
    else:
        return HttpResponse("권한이 없습니다.")
    
    
# ============================= 게시글 좋아요 =============================     
@require_POST
def hearts(request, id):
    if request.user.is_authenticated: # 로그인 인증 여부
        
        post = Post.objects.get(id=id)

        if post.hearts.filter(pk=request.user.id).exists():
            post.hearts.remove(request.user)
        else:
            post.hearts.add(request.user)
        return redirect('detail', post.id) 
    return redirect('sign-in')