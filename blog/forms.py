from django import forms
from .models import Post, Category


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
            'subheading': forms.Textarea(attrs={'rows': 4}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }
