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
    keyword = request.GET['search']
    
    lang = Books._meta.get_field('language')
    cat = Books._meta.get_field('category')
    
    try: 
        choice_lang = request.GET['lang']
    except:
        choice_lang = [l[0] for l in lang.choices]
        
    try: 
        choice_cat = request.GET['cat']
    except:
        choice_cat = [l[0] for l in cat.choices]
        
    print(keyword, choice_lang, choice_cat)
    
    queries = []
    
    
    queries.append(Books.objects.filter(title__icontains=keyword))
    queries.append(Books.objects.filter(author__icontains=keyword))
    queries = [query for search in queries for query in search if query]
    #available = [(book.availability - book.issued) for book in queries]
    print('run')

    
    #data = {'books': queries, 'available':  available}
    data = {'books': queries, 'lang': lang.choices, 'cat': cat.choices, 
            'choice_lang': choice_lang, 'choice_cat': choice_cat, 'search': keyword}
    
    return render (request, 'Home/home.html', data)


def help(request):
    return render (request, 'FAQ/help.html')

def info(request):
    return render (request, 'AboutUs/info.html')

def donate(request):
    return render (request, 'AboutUs/donate.html')

def category(request):
    
    lang = Books._meta.get_field('language')
    
    data = {'lang': lang.choices}
    
    return render (request, 'Home/category.html', data)