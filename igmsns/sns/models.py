from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# 게시글 테이블 모델
class Post(models.Model):
    class Meta:
        db_table = "posting"
        
    post_author = models.CharField("닉네임", max_length=15, default='')
    '''
    글 상세페이지와 글 목록에 사용하는 작성자 이름입니다. 로그인 된 회원의 nickname이 들어갑니다.
    원래는 작성자를 user모델의 외래키로 받아와서 쓰려고 했으나 
    view 함수에서 '현재 로그인 된 사용자의 nickname'을 바로 받아오는 방법이 좋을 것 같아 
    외래키로 지정하지 않고 varchar 형식의 필드가 되었습니다.
    '''
    
    post_title = models.CharField("글제목", max_length=45)
    post_content = models.TextField("글내용")
    post_img = models.FileField("이미지", upload_to='',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
