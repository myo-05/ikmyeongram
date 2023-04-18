# user/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django import forms

# ============================= 기본 유저 모델 상속한 유저모델 ============================= 
class UserModel(AbstractUser):  # UserModel에서 AbstractUser(장고기본유저모델)를 사용하겠다
    class Meta:
        db_table = "my_user"  # 여기는 테이블 이름이에요! 꼭 기억 해 주세요!

    # 기본 모델에 없던 것만 추가 (닉네임, 프로필이미지)
    nickname = models.CharField(max_length=15, default='')
    user_img = models.FileField("프로필이미지",upload_to='',blank=True,null=True,validators=[MaxValueValidator(500 * 1024)], )
    fields = ['nickname', 'user_img']
    
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    '''
    팔로우 필드입니다. 좋아요와 다르게 user 모델 스스로를 many to many 
    symmetrical : 대칭 여부 설정, 만약 True 라고 한다면 저절로 맞팔이 되는 거겠죠?
    '''
    def clean_user_img(self):
        user_img = self.cleaned_data.get('user_img', False)
        if user_img:
            if user_img.size > 500 * 1024:
                raise forms.ValidationError("프로필 이미지의 파일 크기가 500KB를 초과합니다.")
        return user_img