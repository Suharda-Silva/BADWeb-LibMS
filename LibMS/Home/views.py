from django.shortcuts import render
from Home.models import Books

# Create your views here.
def getBooks(request):
    keyword = request.GET.get('key')
    
    queries = []
    queries.append(Books.objects.filter(title__icontains=keyword))
    queries.append(Books.objects.filter(author__icontains=keyword))
    queries = [query for search in queries for query in search if query]
    #available = [(book.availability - book.issued) for book in queries]
    
    #data = {'books': queries, 'available':  available}
    data = {'books': queries}
    
    return render (request, 'Home/home.html', data)
