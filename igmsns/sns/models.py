from django.conf import settings
from django.db import models

# 게시글 테이블 모델
class Post(models.Model):
    class Meta:
        db_table = "posting"
    # user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts') #유저의 아이디
    
    post_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts') # 유저 모델의 사용자를 상속받습니다.
    
    post_title = models.CharField("글제목", max_length=45)
    post_content = models.TextField("글내용")
    post_img = models.FileField("이미지", upload_to='',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author_id = models.CharField(max_length=45)
