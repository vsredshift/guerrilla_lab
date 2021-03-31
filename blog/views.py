from django.shortcuts import render
# from django.http import HttpResponse   # not needed with render

# dummy posts
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


def home(request):
    # return HttpResponse('<h1>Blog Home</h1>')  # without templates for demonstration
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)  # context passes data into template to access keyname within template


def about(request):
    return render(request, 'blog/about.html')

