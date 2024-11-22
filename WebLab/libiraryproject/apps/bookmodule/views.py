from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.db.models import Q
from django.db.models import Count, Sum,Max,Min,Avg
from django.shortcuts import  redirect, get_object_or_404
from .forms import BookForm


def index(request):
 return render(request, "bookmodule/index.html")
def list_books(request):
 return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
 return render(request, 'bookmodule/one_book.html')
def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')
def viewlinks(request):
 return render(request, 'bookmodule/links.html')
def viewFormat(request):
 return render(request, 'bookmodule/formating.html')
def viewListing(request):
 return render(request, 'bookmodule/listing.html')
def viewTable(request):
 return render(request, 'bookmodule/tables.html')


def viewSearch(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
 # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})

    return render(request,'bookmodule/search.html')
    


def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def createBook(request):
    mybook = Book(title = 'Continuous Delivery', author = 'J.Humble and D. Farley', edition = 1)
    mybook.save()
    return HttpResponse("Book created successfully")

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks = mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def lab8_task1(request):
   mybooks = Book.objects.filter(Q(price__lte = 50))
   return render(request, 'bookmodule/booklist.html',{'books':mybooks})

def lab8_task2(request):
   mybooks = Book.objects.filter(Q(edition__gt = 2) & (Q(title__icontains='qu')|Q(author__icontains='qu')))
   return render(request, 'bookmodule/booklist.html',{'books':mybooks})

def lab8_task3(request):
    mybooks = Book.objects.filter(~Q(edition__gt = 2) & (~Q(title__icontains='qu')|~Q(author__icontains='qu')))
    return render(request, 'bookmodule/booklist.html',{'books':mybooks})

def lab8_task4(request):
   mybooks = Book.objects.all().order_by('title')
   return render(request, 'bookmodule/booklist.html',{'books':mybooks})

def lab8_task5(request):
    mybooks = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/Lab8_task5.html',{'books':mybooks})

def lab9_task1(request):
   mybooks=Book.objects.filter(title__icontains='and')
   return render(request, 'bookmodule/lab9_task1.html',{'books':mybooks})

def add_book(request):
     if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = float(request.POST.get('price'))
        edition = int(request.POST.get('edition'))

        Book.objects.create(
            title=title,
            author=author,
            price=price,
            edition=edition
        )
        return redirect('/books/lab9_part1/listbooks')
     return render(request, 'bookmodule/add.html')


def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = float(request.POST.get('price'))
        book.edition = int(request.POST.get('edition'))
        book.save()
        return redirect('/books/lab9_part1/listbooks')  # Update redirect URL

    return render(request, 'bookmodule/edit.html', {'book': book})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('/books/lab9_part1/listbooks') 

def add_book2(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('/books/lab9_part1/listbooks') 
    else:
        form = BookForm()  
    
    return render(request, 'bookmodule/add_book2.html', {'form': form})


def edit_book2(request, id):
    book = get_object_or_404(Book, id=id)  # Get the book by its id
    
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)  # Bind the form to the book instance
        if form.is_valid():
            form.save()  # Save the updated book
            return redirect('/books/lab9_part1/listbooks')  # Redirect to book list after saving
    else:
        form = BookForm(instance=book)  # Create a form with existing book data
    
    return render(request, 'bookmodule/edit_book2.html', {'form': form, 'book': book})