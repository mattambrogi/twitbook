# articles/urls.py
from django.urls import path
from .views import FeedListView, PostDeleteView, PostCreateView, PostDetailView, CommentDeleteView

urlpatterns = [
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/delete_comment/', CommentDeleteView.as_view(), name='comment_delete'),  
    path('<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('', FeedListView.as_view(), name='feed_list'),
]