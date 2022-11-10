from django.contrib import admin

from .models import Article


# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "description", "content", "thumbnail", "image_content", "date", "author", "isPublished")
    list_editable = ("slug", "isPublished", "thumbnail", "image_content", "content", "description")


admin.site.register(Article, ArticleAdmin)
