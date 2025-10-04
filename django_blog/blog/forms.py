from django import forms
from django.contrib.auth.forms import UserCreationForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']

# add validation if needed
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("Content is required.")
        return content
