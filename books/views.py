from django.shortcuts import render, HttpResponseRedirect
from .forms import BookRegister
from .models import Books
# Create your views here.
# This method is used to Update book
def add_show_book(request):
    if request.method == 'POST':
        fm = BookRegister(request.POST)
        if fm.is_valid():
            author_name = fm.cleaned_data['author_name']
            book_name = fm.cleaned_data['book_name']
            reg = Books(author_name=author_name, book_name=book_name)
            reg.save()
            fm = BookRegister() #to make the form blank
    else:
        fm = BookRegister()
    books = Books.objects.all()
    return render(request, 'books/addandshow.html', {'form': fm, 'books': books})

# This method is used to Update book
def update_book(request, id):
    if request.method == 'POST':
        book_data = Books.objects.get(pk=id)
        fm = BookRegister(request.POST, instance=book_data)
        if fm.is_valid():
            fm.save()
    else:
        book_data = Books.objects.get(pk=id)
        fm = BookRegister(instance=book_data)
    return render(request, 'books/updatebook.html', {'form': fm})

# This method is used to Delete book
def delete_book(request, id):
    if request.method == 'POST':
        book_data = Books.objects.get(pk=id)
        book_data.delete()
        return HttpResponseRedirect('/')