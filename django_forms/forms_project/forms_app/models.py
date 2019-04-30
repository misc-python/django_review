from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)
    description = models.CharField(max_length=264, default='default description')

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class UserProfileInfo(models.Model):
    """Create a one-to-one model relationship to User."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
