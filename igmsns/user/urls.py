from django.urls import path
from user import views

urlpatterns = [
    path('sign-in/', views.sign_in_view, name='sign-in'), # 로그인
    path('sign-out/', views.logout, name = 'sign-out'), # 로그아웃
    path('sign-up/', views.sign_up,name='sign-up'), # 회원가입
    path('<int:user_id>/follow/', views.follow, name = 'follow'), # 팔로우
    path('following-list/<int:id>/', views.following_list, name='following-list'),
    path('follower-list/<int:id>/', views.follower_list, name='follower-list'),
]