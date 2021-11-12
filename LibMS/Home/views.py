from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.decorators import login_required
from Home.models import Books, UserBook
from django.contrib import messages

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
    return render (request, 'Home/category.html')

def selectedBook(request, error=None):
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
    
    userBooks_max = False
    userBooks = UserBook.objects.filter(user=request.user)
    if len(userBooks) >= 3:
        userBooks_max = True
    
    #print(userBooks, len(userBooks), userBooks_max)
    
    data = {'selected': book[0], 'lang': lang_long[lang_id], 'cat': cat_long[cat_id], 'userBooks': userBooks_max, 'error': error}
    
    return render (request, 'Home/home.html', data)


def reserveBook(request):
    reserve = request.GET['reserve']
    id = request.GET['id']
    
    if reserve:
        book = Books.objects.filter(id=id)[0]
        userBooks = UserBook.objects.filter(user=request.user)
        userBooks = [book.book.title for book in userBooks]
        
        print(book, userBooks, str(book) in userBooks)
        
        if str(book) not in userBooks:
            print('run')
            UserBook.objects.create(user=request.user, book=book)
            book.issued += 1
            book.save()
        else:
            print('error')
            error = 'A user can only reserve one copy of a book at a time !'
            return selectedBook(request, error)
        
    return selectedBook(request)


def myBooks(request):
    
    userBooks = UserBook.objects.filter(user=request.user)
    data = {'books': userBooks}
    
    return render(request, 'User/myBooks.html', data)

def removeBook(request):
    
    id = request.GET['id']
    Ubook_I = UserBook.objects.filter(id=id)
    Ubook = Ubook_I[0].book
    book = Books.objects.filter(title=Ubook)[0]
    print(book)
    book.issued -= 1
    book.save()
    
    Ubook_I.delete()
    
    
    
    return myBooks(request)