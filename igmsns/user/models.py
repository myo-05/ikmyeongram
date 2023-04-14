# user/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# ============================= 기본 유저 모델 상속한 유저모델 ============================= 
class UserModel(AbstractUser):  # UserModel에서 AbstractUser(장고기본유저모델)를 사용하겠다
    class Meta:
        db_table = "my_user"  # 여기는 테이블 이름이에요! 꼭 기억 해 주세요!

    # 기본 모델에 없던 것만 추가 (닉네임, 프로필이미지)
    nickname = models.CharField(max_length=15, default='')


#===============유저의 프로필 이미지를 저장할 테이블 | 기본 유저 모델은 img업로드가 불가!================
class UserImg(models.Model):
    class Meta:
        db_table = "my_user_img" # 여기는 테이블 이름이에요! 꼭 기억 해 주세요!
        
    users_img = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    user_img = models.FileField("프로필이미지", upload_to='profile_img',blank=True, null=True)