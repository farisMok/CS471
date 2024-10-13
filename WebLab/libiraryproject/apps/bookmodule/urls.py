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
]
