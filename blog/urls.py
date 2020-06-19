from django.urls import path
from .views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
	UserPostListView,
    TaggedPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:post_id>/comment/', views.comment, name='comment'),
    path('post/<int:post_id>/<int:comment_id>/delete/', views.comment_delete, name='comment-delete'),
    path('post/<int:post_id>/tag/', views.tag_create, name='tag'),
    path('tag/<str:tag>/', TaggedPostListView.as_view(), name='tagged-posts'),
    path('about/', views.about, name='blog-about'),
]
