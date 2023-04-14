from django.urls import path
from sns import views

urlpatterns = [
    path('', views.home, name='home'),  # /api/sns/
    path('new/', views.new, name='new'), # /api/sns/new
    path('post/', views.new_post_view, name='post'),  # /api/sns/post/
    path('post/<int:id>/', views.detail_post_view, name = 'detail'),  # /api/sns/post/<id>/ 게시글 상세 페이지
    path('post/<int:id>/delete/', views.delete, name='delete'),# /api/post/{Post_id}/ 게시글 삭제
    path('post/<int:id>/update/', views.update, name='update'),  # /api/post/{Post_id}/ 게시글 수정 페이지
        
    path('post/<int:id>/comment/', views.comment_create, name='comment'),  # /api/sns/post/<id>/comment/ 댓글 작성하기
    path('post/<int:id>/comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),  # /api/sns/post/<id>/comment/<comment_id>/delete 댓글 삭제하기
    path('post/<int:id>/comment/<int:comment_id>/edit/', views.comment_edit, name='comment_edit'),
    path('profile/<str:author_id>/', views.profile_view, name='profile'),  # /api/sns/profile/<id>/ 프로필페이지
]