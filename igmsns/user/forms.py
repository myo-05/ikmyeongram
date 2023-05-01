from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import UserModel


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ['username', 'nickname', 'user_img']