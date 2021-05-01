from django import forms
from .models import Post, Category, Comment
from mptt.forms import TreeNodeChoiceField


class PostForm(forms.ModelForm):
    class Meta:
        list_categories = Category.objects.all().values_list(
            'category_name', 'category_name')
        choices = []
        for i in range(len(list_categories)):
            choices.append(list_categories[i])
            choices.sort()

        model = Post
        fields = ('title', 'subheading', 'head_image',
                  'category', 'tags', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subheading': forms.Textarea(attrs={'rows': 3}),
            'head_image': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    class MPTTMeta:
        model = Comment
        fields = ('body', 'parent')
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

class FeaturedPost(PostForm):
    
    class Meta:
        fields = ('featured','title', 'subheading', 'head_image',
                  'category', 'tags', 'content')
        model = Post