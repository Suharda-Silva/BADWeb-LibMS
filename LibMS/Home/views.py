from django.shortcuts import render
from Home.models import Books

# Create your views here.
DATA_FORMAT = {
    'id':[],
    'name':[]
}


def getBooks(request):
    keyword = request.GET.get('key')
   
    ### Database
    q="harry"
    queries = []
    queries.append( Books.objects.filter(title__icontains=q))
    queries.append(Books.objects.filter(author__icontains=q))
    print(queries)
    
    data = DATA_FORMAT
    
    data['id'].append('01')
    data['name'].append('Sample Book')
    
    return render (request, 'Home/home.html',data)
