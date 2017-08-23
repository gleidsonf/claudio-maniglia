from django.db import models
from django.utils import timezone
from django.conf import settings

class Type(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=70)

    def create(self):
        self.save()

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    type_post = models.ForeignKey('blog.Type')
    photo = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/no-image.png')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url