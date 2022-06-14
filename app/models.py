from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/',default='default.png')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    name = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    @classmethod
    def update_profile(cls, id, value):
        cls.objects.filter(id=id).update(profile_picture=value)

    def save_profile(self):
        self.name
    def delete_profile(self):
        self.delete()
        
    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


class Post(models.Model):
    title = models.CharField(max_length=155)
    image = models.ImageField(upload_to='post/', blank=True) 
    url = models.URLField(max_length=255)
    technologies = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    description = models.TextField(max_length=255)

    def __str__(self):
        return f'{self.title}'