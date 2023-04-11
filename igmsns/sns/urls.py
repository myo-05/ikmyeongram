from django.urls import path

from sns import views

urlpatterns = [
    path('', views.home, name='home'),  # /api/sns/ 실제 주소창에 보이는 주소 
    path('new/', views.new, name='new'), # /api/sns/new 실제 주소창에 보이는 주소
    path('post/', views.new_post_view, name='post'),  # /api/sns/post/ 실제 주소창에 보이는 주소

]

