from django.contrib import admin

# Register your models here.
from posts.models import Post


@admin.register(Post)
class PostModel(admin.ModelAdmin):
    pass
