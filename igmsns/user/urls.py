from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('sign-up-detail/', views.sign_up_detail), # 정은 : 임시로 만들었습니다
]
