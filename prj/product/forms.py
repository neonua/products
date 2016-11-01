from django import forms
from models import Comment


class CommentForm(forms.ModelForm):
    """Comment form"""
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                           error_messages={
                               'required': 'You have not entered a name!'
                            })

    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),
                           error_messages={
                               'required': 'You have not entered a message!'
                           })
    class Meta:
        model = Comment
        fields = ('name', 'body')
        labels = {
            "name": "Your name",
            "body": "Your text"
        }
