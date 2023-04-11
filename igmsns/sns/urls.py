from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_view, name="home"), # /api/sns/
    path('post/', views.post_view, name="post-list"), # /api/sns/post/
]