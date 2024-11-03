from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('html5/links', views.viewlinks, name="books.links"),
 path('html5/text/formatting', views.viewFormat, name="books.format"),
 path('html5/listing', views.viewListing, name="books.listing"),
 path('html5/tables',views.viewTable, name="books.tables"),
 path('search/',views.viewSearch,name='books.search'),
 path('create/',views.createBook,name="book.create"),
 path('simple/query/',views.simple_query, name="book.simple_query"),
 path('complex/query/',views.complex_query,name="book.complex_query"),
 path('lab8/task1',views.lab8_task1,name="Lab8_Task1"),
 path('lab8/task2',views.lab8_task2,name="Lab8_Task2"),
 path('lab8/task3',views.lab8_task3,name="Lab8_Task3"),
 path('lab8/task4',views.lab8_task4,name="Lab8_Task4"),
 path('lab8/task5',views.lab8_task5,name="Lab8_Task5"),  
]
