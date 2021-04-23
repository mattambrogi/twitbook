# articles/admin.py
from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline): # new
    model = Comment

class FeedAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Post)
admin.site.register(Comment)