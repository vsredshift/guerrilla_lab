from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, CategoryView, LikePostView, DislikePostView
from users.views import ProfilePageView
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

    # Route to specific post using slug
    path('post/<slug>/', PostDetailView.as_view(), name='post-detail'),

    # Create a new post [template <model>_<form>]
    path('post/', PostCreateView.as_view(), name='post-create'),

    # Update Post
    path('post/<slug>/update/', PostUpdateView.as_view(), name='post-update'),

    # Delete Post
    path('post/<slug>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Posts by category
    path('category/<str:category>/', CategoryView, name='category'),

    # Likes/Dislikes
    path('like/<slug>/', LikePostView, name="post-like"),
    path('dislike/<slug>/', DislikePostView, name="post-dislike"),

    # User Profile Page
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='profile-page'),
    # About Page
    path('about/', views.about, name='blog-about'),
]


# Add media files if in dev mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
