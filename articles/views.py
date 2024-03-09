from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def articles_list(request):
    articles = Article.objects.all().order_by("date")
    return render(request, 'articles/article_list.html',{"articles":articles})

def article_detail(request, slug):
    # Retrieve the article based on the slug
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        # Handle the case where the article with the given slug doesn't exist
        return render(request, '404.html', {})  # Replace with your 404 template

    # Pass the retrieved article to the template context and render it
    context = {'article': article}
    return render(request, 'articles/article_detail.html', context)


@login_required(login_url="accounts:login")
def article_create(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form })
