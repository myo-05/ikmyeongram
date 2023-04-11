from django.urls import path
from sns import views

urlpatterns = [
    path('', views.home, name='home'),  # /api/sns/
    path('new/', views.new, name='new'),  # /api/sns/new
    path('post/', views.new_post_view, name='post'),  # /api/sns/post/
]
