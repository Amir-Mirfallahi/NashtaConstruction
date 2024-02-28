from django.contrib import admin
from unfold.admin import ModelAdmin

from .forms import PostForm
from .models import Post, Topic


@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ('title', 'author', 'publish_date', 'views')
    search_fields = ('title', 'author', 'publish_date', 'topic')
    form = PostForm


@admin.register(Topic)
class TopicAdmin(ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
