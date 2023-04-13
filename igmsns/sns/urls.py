from django.urls import path
from sns import views

urlpatterns = [
    path('', views.home, name='home'),  # /api/sns/
    path('new/', views.new, name='new'), # /api/sns/new
    path('post/', views.new_post_view, name='post'),  # /api/sns/post/
    path('post/<int:id>/', views.detail_post_view),  # /api/sns/post/<int:id>/ 게시글 상세 페이지
    path('post/<int:id>/delete/', views.delete, name='delete'),# /api/post/{Post_id}/ 게시글 삭제
    path('post/<int:id>/update/', views.update, name='update'),  # /api/post/{Post_id}/ 게시글 수정 페이지
    path('profile/<str:post_author>/', views.profile_view),  # /api/sns/profile/<int:id>/ 프로필페이지
]
