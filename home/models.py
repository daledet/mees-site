from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class NewsLetter(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(
        null=True, blank=True, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)


class NewsletterImage(models.Model):
    newsletter = models.ForeignKey(NewsLetter, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True,
                              upload_to='images/')


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    description = models.TextField()
    website_url = models.CharField(max_length=255, null=True, blank=True)
    event_date = models.DateField('MM/DD/YYYY',
                                  auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.name


class PastEvent(models.Model):
    event_name = models.CharField(max_length=255)
    header_image = models.ImageField(
        null=True, blank=True, upload_to='images/')
    event_date = models.CharField(max_length=30)
    event_location = models.CharField(max_length=100)
    event_description = RichTextField(blank=True, null=True)
    order_date = models.DateField('MM/DD/YYYY',
                                  auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.event_name


class About(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(
        null=True, blank=True, upload_to='images/')
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title
