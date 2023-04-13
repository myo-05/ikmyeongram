from django.conf import settings
from django.db import models

from user.models import UserModel

# ============================= 게시글 테이블 모델 =============================    
class Post(models.Model):
    class Meta:
        db_table = "my_posting"
    
    post_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts') # 글 작성자 : 유저 모델의 사용자를 상속받습니다.
    post_title = models.CharField("글제목", max_length=45)
    post_content = models.TextField("글내용")
    post_img = models.FileField("이미지", upload_to='',blank=True, null=True) # 글 내 이미지 업로드
    created_at = models.DateTimeField(auto_now_add=True) # 생성시각
    updated_at = models.DateTimeField(auto_now=True) # 수정시각
    author_id = models.CharField(max_length=45) # 현재 로그인 중인 유저의 기본키 넣을 자리

# ============================= 댓글 테이블 모델 =============================    
class Comment(models.Model):
    class Meta:
        db_table = "my_comment"
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    