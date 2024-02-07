from django.contrib import admin
from .models import Category, Label, Blog


class BlogContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_blog_title',)

    def get_blog_title(self, obj):
        return obj.blog.title
    get_blog_title.short_description = 'Blog Adı' 

    

# Register your models here.
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Label) 

