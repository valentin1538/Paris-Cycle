from django.shortcuts import render
from .models import Article

def index(request):
    # On récupère les 3 dernières actualités
    articles = Article.objects.all().order_by('-date_publication')[:3]
    return render(request, 'core/index.html', {'articles': articles})