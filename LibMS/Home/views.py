from django.shortcuts import render
from Home.models import Books

# Create your views here.
def getBooks(request):
    keyword = request.GET.get('key')
    
    print(keyword)
    queries = []
    queries.append(Books.objects.filter(title__icontains=keyword))
    queries.append(Books.objects.filter(author__icontains=keyword))
    
    print(queries)
    data = {'books': queries}
    
    return render (request, 'Home/home.html', data)
