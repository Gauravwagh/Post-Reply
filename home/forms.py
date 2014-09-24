from django import forms
from home.models import Post, Comment, UserProfile
#from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        #model= profile
        model = Post
        
        widgets = {
                   'post': forms.Textarea(attrs={'cols':80, 'rows':20}),
                   }
        
class CommentForm(forms.ModelForm):
    class Meta:
        #model= profile
        model = Comment
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        #model= profile
        model = UserProfile