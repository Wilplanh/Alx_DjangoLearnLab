from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, tag
from taggit.forms import TagWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'tags': TagWidget(),
        }

# add validation if needed
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("Content is required.")
        return content


