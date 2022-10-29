from django.contrib import admin


from .models import Comment, Follow, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'post', 'author')
    search_fields = ('text', 'post', 'author')
    list_filter = ('pub_date', 'author')
    empty_value_display = '-пусто-'


admin.site.register(Follow)
admin.site.register(Group)
