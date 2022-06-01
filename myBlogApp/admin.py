from django.contrib import admin
from . models import Post, Comment
# Register your models here.


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_posted', 'user', 'comment']
    search_fields = ['title']
    inlines = [
        CommentInline,
    ]

    def comment(self, comment):
        return comment.content
