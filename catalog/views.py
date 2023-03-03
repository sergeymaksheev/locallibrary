from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre
# Create your views here.

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  
    num_genre = Genre.objects.all().count()
    num_witcher = Book.objects.filter(title__icontains='ведьмак').count()
    
    # Метод 'all()' применён по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,
                 'num_instances_available':num_instances_available,'num_authors':num_authors, 
                 'num_genre': num_genre, 'num_witcher': num_witcher
                 },
    )

class BookListView(generic.ListView):

    queryset = Book.objects.all()
    template_name = "catalog/templates/catalog/book_list.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(BookListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и инициализируем её некоторым значением
        context['some_data'] = 'This is just some data'
        return context
     

class BookDetailView(generic.DetailView):

    model = Book


class AuthorListView(generic.ListView):

    queryset = Author.objects.all()
    template_name = "catalog/templates/catalog/author_list.html"
    paginate_by = 2


class AuthorDetailView(generic.DetailView):

    model = Author