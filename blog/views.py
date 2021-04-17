from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect as redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django import forms
from django.core.paginator import Paginator
from django.template.defaultfilters import slugify
from django.urls import reverse
from taggit.models import Tag

# Class views
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm

"""
dummy posts to get started
posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]
"""

""" Function View """
# def home(request):
#     # return HttpResponse('<h1>Blog Home</h1>')  # without templates for demonstration
#     context = {
#         # 'posts': posts    # Dummy posts
#         'posts': Post.objects.all()
#     }
#     # context passes data into template to access keyname within template
#     return render(request, 'blog/home.html', context)


""" Class View """


class PostListView(ListView):
    model = Post
    # Create template to handle class view
    template_name = 'blog/home.html'    # <app>/<model>_<viewtype>.html
    title = 'Blog Home'
    # set name to use in template instead of default "object_list"
    context_object_name = 'posts'

    ordering = ['-date_posted']         # Show newest posts first
    paginate_by = 5                     # Set number of posts per page

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu.order_by('category_name')
        context['title'] = self.title
        return context


class UserPostListView(ListView):
    # show only posts of selected user
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # use order_by since ordering overridden as part of queryset override
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    # fields = ['title', 'subheading', 'category', 'content']

    # Override form_valid method and set author to current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    # fields = ['title', 'subheading', 'category', 'content']

    # Override form valid method and set author to current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Ensure only author of post can update current post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'       # Send to home after deletion

    # Ensure only author of post can update current post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def CategoryView(request, category):
    category_posts = Post.objects.filter(
        category=category.casefold().capitalize()).order_by('-date_posted')
    paginator = Paginator(category_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_category.html', {'category': category, 'page_obj': page_obj})


def LikePostView(request, slug):
    post = get_object_or_404(Post, slug=request.POST.get('post_id'))
    post.likes.add(request.user)
    return redirect(reverse('post-detail', args=[slug]))


def DislikePostView(request, slug):
    post = get_object_or_404(Post, slug=request.POST.get('post_id_down'))
    post.dislikes.add(request.user)
    return redirect(reverse('post-detail', args=[slug]))
