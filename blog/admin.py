from django.contrib import admin
from .models import Post, Type, Curso, Foto
# Register your models here.

admin.site.register(Type)
admin.site.register(Post)
admin.site.register(Curso)
admin.site.register(Foto)
