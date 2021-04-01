from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    # Function View
    # path('', views.home, name='blog-home'),   

    # Class View. Needs template <app>/<model>_<viewtype>.html
    path('', PostListView.as_view(), name='blog-home'),    
    # Posts by user
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),  
    # Route to specific post using integer:primary key (convention)
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), 
    # Create a new post [template <model>_<form>]
    path('post/new/', PostCreateView.as_view(), name='post-create'),  
    # Update Post
     path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),   
    # Delete Post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),   

    path('about/', views.about, name='blog-about'),
]