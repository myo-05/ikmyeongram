from django.urls import path
from sns import views

urlpatterns = [
    path('', views.home, name='home'),  # 모든 글 리스트보여주는 홈 페이지 
    path('new/', views.new, name='new'), # 새 글 작성 페이지로 렌더링
    path('post/', views.new_post_view, name='post'),  # # 새 글 작성 저장
    path('post/<int:id>/', views.detail_post_view, name = 'detail'),  # 게시글 상세 페이지
    path('post/<int:id>/delete/', views.delete, name='delete'),#  게시글 삭제
    path('post/<int:id>/update/', views.update, name='update'),  #  게시글 수정 페이지
        
    path('<int:id>/hearts/', views.hearts, name='hearts'),    # 게시글 좋아요
        
    path('post/<int:id>/comment/', views.comment_create, name='comment'),  # 댓글 작성하기
    path('post/<int:id>/comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),  #  댓글 삭제하기
    path('post/<int:id>/comment/<int:comment_id>/edit/', views.comment_edit, name='comment_edit'), # 댓글 수정하기
    
    path('profile/<int:author_id>/', views.profile_view, name="profile"),  # 프로필페이지
    path('profile/<int:author_id>/<str:type>', views.profile_postlist_view, name="profilepost"),  #  프로필페이지
    

]