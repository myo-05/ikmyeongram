from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required

# 정은 : 게시글 리스트 불러오기는 회원이랑 비회원 접근이 가능하기 때문에 바로 렌더 되게 해줬습니다!
def product_view(request):
    if request.method == 'GET':
        all_post = Post.objects.all().order_by('-created_at')
        return render(request, 'sns/home.html',{'post':all_post})

def post_view(request):
    return HttpResponse('화 좀 그만 내...')