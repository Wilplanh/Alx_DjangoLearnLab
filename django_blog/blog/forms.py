from django import forms
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.Form):
    author = forms.CharField(max_length=100, label='Your Name')
    content = forms.CharField(widget=forms.Textarea, label='Your Comment')

# add validation if needed
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("Content is required.")
        return content
