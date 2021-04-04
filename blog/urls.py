from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, CategoryView, LikePostView, DislikePostView
from . import views
# Serving static files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Function View
    # path('', views.home, name='blog-home'),   

    # Class View. Uses template <app>/<model>_<viewtype>.html
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

    # Posts by category
    path('category/<str:category>/', CategoryView, name='category'),

    path('like/<int:pk>/', LikePostView, name="post-like"),
    path('dislike/<int:pk>/', DislikePostView, name="post-dislike"),

    # About Page
    path('about/', views.about, name='blog-about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)