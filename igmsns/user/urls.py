from django.urls import path
from user import views

urlpatterns = [
   
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('sign-out/', views.logout, name = 'sign-out'),
    path('sign-up-detail/', views.sign_up_detail,name='sign-up'), # 정은 : 임시로 만들었습니다
]