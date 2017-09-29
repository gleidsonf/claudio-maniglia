from django.contrib import admin
from .models import Post, Type, Curso
# Register your models here.

admin.site.register(Type)
admin.site.register(Post)
admin.site.register(Curso)
