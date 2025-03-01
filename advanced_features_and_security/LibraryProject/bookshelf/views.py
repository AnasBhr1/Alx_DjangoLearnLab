# Create your views here.
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Article
from .forms import ExampleForm

@permission_required("app_name.can_view", raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, "articles/list.html", {"articles": articles})

@permission_required("app_name.can_create", raise_exception=True)
def create_article(request):
    # Logic for creating an article
    pass

@permission_required("app_name.can_edit", raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    # Logic for editing an article
    pass

@permission_required("app_name.can_delete", raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect("article_list")

from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
