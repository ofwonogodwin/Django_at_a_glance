from django.shortcuts import render,redirect

from .models import Article

# Create your views here.

def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {"year": year, "article_list": a_list}
    return render(request, "news.html", context)

def home_redirect(request):
    return redirect('year-archive', year=2025)  # or any default year