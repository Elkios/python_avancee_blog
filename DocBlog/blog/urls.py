from django.urls import path

from .views import index, article, BlogHome, ArticleCreate, ArticleDelete, ArticleEdit

app_name = "blog"

urlpatterns = [
    path('index/', index, name="blog-index"),
    path('article/<str:numero_article>/', article, name="blog-article"),
    path('', BlogHome.as_view(), name="blog-home"),
    path('addarticle/', ArticleCreate.as_view(), name="blog-add_article"),
    path('delete/<str:slug>/', ArticleDelete.as_view(), name="delete"),
    # edit
    path('edit/<str:slug>/', ArticleEdit.as_view(), name="edit"),
]
