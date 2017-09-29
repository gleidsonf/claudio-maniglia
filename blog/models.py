from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


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
    title = models.CharField(max_length=30)
    text = RichTextUploadingField(config_name='awesome_ckeditor')
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


class Contact(models.Model):
    name = models.CharField(max_length=70, blank=False)
    email = models.CharField(max_length=100, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=False) # validators should be a list
    message = models.TextField()

    def __str__(self):
        return self.name


class Curso(models.Model):
    titulo = models.CharField(max_length=120, blank=False)
    local = models.CharField(max_length=120, blank=False)
    duracao = models.CharField(max_length=50, blank=True)
    data_inicio = models.DateTimeField(blank=False)
    data_termino = models.DateTimeField(blank=False)

    def __str__(self):
        return self.titulo
