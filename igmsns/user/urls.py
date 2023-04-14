from django.urls import path
from user import views

urlpatterns = [
    path('sign-in/', views.sign_in_view, name='sign-in'), # 로그인
    path('sign-out/', views.logout, name = 'sign-out'), # 로그아웃
    path('sign-up-detail/', views.sign_up_detail,name='sign-up'), # 회원가입
]