from django import forms
from .models import Profile,Post

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_picture', 'contact', 'bio']

class UploadProjectForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'url', 'technologies','description']