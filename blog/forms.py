from .models import Comment, Post
from django import forms
from django.shortcuts import render, get_object_or_404

class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.slug = kwargs.pop('slug')
        super().__init__(*args, **kwargs)
        post = get_object_or_404(Post, slug=self.slug)
        comments = post.comments.filter(active=True, replay=None)
        self.fields['replay'] = forms.ModelChoiceField(queryset=comments, required=False)
        #self.fields['name'].initial = ''
        #replay = forms.ModelChoiceField(queryset=comments)

    class Meta:
        model = Comment
        fields = ('replay', 'name', 'email', 'body')