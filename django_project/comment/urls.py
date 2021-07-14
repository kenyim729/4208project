from django.urls import path
from .views import (
    CommentListView,
    CommentDetailView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)
from . import views

urlpatterns = [
    path('Forum/', CommentListView.as_view(), name='blog-forum'),
    path('post/<int:pk>/', CommentDetailView.as_view(), name='post-detail'),
    path('post/new/', CommentCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', CommentUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', CommentDeleteView.as_view(), name='post-delete'),
]
