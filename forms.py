from django import forms
from core.models import Comment

class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=1000, required=True)

    class Meta:
        model = Comment
        fields = ('text',)
