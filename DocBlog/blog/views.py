from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from .models import Article
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import UpdateView

# Create your views here.

def index(request):
    return render(request, "blog/index.html")

class ArticleCreate(CreateView):
    model = Article
    success_url = reverse_lazy("blog:blog-home")
    template_name = 'blog/add_article.html'
    fields = ['title', 'slug', 'description', 'content', 'author', 'thumbnail', 'image_content']


class ArticleDetail(DetailView):
    model = Article
    context_object_name = "post"

class ArticleEdit(UpdateView):
    model = Article
    template_name = 'blog/article_edit.html'
    fields = ['title', 'content']
    success_url = reverse_lazy("blog:blog-home")

class ArticleDelete(DeleteView):
    model = Article
    success_url = reverse_lazy("blog:blog-home")

class BlogHome(ListView):
    model = Article
    context_object_name = "posts"

def add_article(request):
    return render(request, "blog/add_article.html")

def article(request, numero_article):
    # Get the article
    article = Article.objects.get(id=numero_article)
    return render(request, f"blog/article.html", context={"article": article})
