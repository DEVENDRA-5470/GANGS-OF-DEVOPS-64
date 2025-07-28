from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', default='profile_images/default.jpg')
    full_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True)
    bio = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    facebook = models.CharField(max_length=500, null=True, blank=True)
    github = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.CharField(max_length=500, null=True, blank=True)
    insta = models.CharField(max_length=500, null=True, blank=True)
    twitter = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.user.username

# Stats model
class Stats(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)  # One-to-One relationship with Profile
    total_downloads = models.IntegerField(null=True, default=0)
    topic_names = models.TextField(null=True, blank=True)
    total_logins = models.IntegerField(null=True, default=0)
    last_login = models.CharField(null=True, blank=True,max_length=200)

    def __str__(self):
        return f"Stats for {self.profile.user.username}"
