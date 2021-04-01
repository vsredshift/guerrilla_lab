from django.shortcuts import render
# from django.http import HttpResponse   # not needed with render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

""" 
dummy posts
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
def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')  # without templates for demonstration
    context = {
        # 'posts': posts    # Dummy posts
        'posts': Post.objects.all()
    }
    # context passes data into template to access keyname within template
    return render(request, 'blog/home.html', context)


""" Class View """
class PostListView(ListView):
    model = Post
    # Create template to handle class view
    template_name = 'blog/home.html'    # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'       # set name to use in template instead of default "object_list"
    ordering = ['-date_posted']         # Show newest posts first


class PostDetailView(DetailView):
    # following convention in template we only need one line of code!!
    model = Post
    
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    
    # Override form valid method and set author to current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
