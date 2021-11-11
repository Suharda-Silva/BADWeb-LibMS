from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.decorators import login_required
from Home.models import Books

#@login_required
@csrf_exempt
def home (request):
    if request.user.is_authenticated:
        return render(request, 'Home/home.html', {'user':request.user})
    else:
        return redirect('/login/')


# Create your views here.
def getBooks(request):
    keyword = request.GET.get('search')
    
    queries = []
    queries.append(Books.objects.filter(title__icontains=keyword))
    queries.append(Books.objects.filter(author__icontains=keyword))
    queries = [query for search in queries for query in search if query]
    #available = [(book.availability - book.issued) for book in queries]
    
    #data = {'books': queries, 'available':  available}
    data = {'books': queries}
    
    return render (request, 'Home/home.html', data)


def help(request):
    return render (request, 'FAQ/help.html')

def info(request):
    return render (request, 'AboutUs/info.html')

def donate(request):
    return render (request, 'AboutUs/donate.html')

def category(request):
    return render (request, 'Home/category.html')