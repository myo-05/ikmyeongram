from django.db import models

# Create your models here.
class Post(models.Model):
    class Meta:
        db_table = "posting"
        
    post_author = models.CharField(max_length=256) # user 모델의 사용자를 상속받습니다. 바뀌어야 합니다.
    post_title = models.CharField(("글제목"), max_length=45)
    post_content = models.TextField("글내용")
    post_img = models.FileField(upload_to='igmsns/static/post')
    """
    html에 들어가야 하는 것
    <form method="post" enctype="multipart/form-data">
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)