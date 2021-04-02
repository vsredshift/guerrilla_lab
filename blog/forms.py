from django import forms
from .models import Post, Category

list_categories = Category.objects.all().values_list()
choices = []
for i in range(len(list_categories)):
    choices.append(list_categories[i])

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subheading', 'category', 'content')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'subheading' : forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.Select(choices=choices, attrs={'class':'form-control'}),
            'content' : forms.Textarea(attrs={'class':'form-control'})
        }