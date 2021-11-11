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
    
    queries = []
    
    
    queries.append(Books.objects.filter(title__icontains=keyword))
    queries.append(Books.objects.filter(author__icontains=keyword))
    queries = [query for search in queries for query in search if query]
    #available = [(book.availability - book.issued) for book in queries]

    
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

def selectedBook(request):
    id = request.GET.get('id')
    book = Books.objects.filter(id=id)
    
    lang_choices = Books._meta.get_field('language').choices
    lang_short = [i[0] for i in lang_choices]
    lang_long = [i[1] for i in lang_choices]
    lang_id = lang_short.index(book[0].language)
    
    cat_choices = Books._meta.get_field('category').choices
    cat_short = [i[0] for i in cat_choices]
    cat_long = [i[1] for i in cat_choices]
    cat_id = cat_short.index(book[0].category)
    
    data = {'selected': book[0], 'lang': lang_long[lang_id], 'cat': cat_long[cat_id]}
    
    return render (request, 'Home/home.html', data)