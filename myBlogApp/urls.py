from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('user/<str:email>', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(template_name='post_create.html'), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(template_name='post_create.html'), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(template_name='post_confirm_delete.html'), name='post_delete')

]
