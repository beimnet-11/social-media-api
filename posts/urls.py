from django.urls import path
from . import views
urlpatterns = [
    path('', views.posts_list_create, name='post_list_create'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/like/', views.like_post, name='like_post'),
    path('<int:post_id>/comments/', views.comments_list_create, name='comments_list_create'),
]