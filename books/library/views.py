from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Books
from django.db.models import Q

def home(request):
    query = request.GET.get('q')
    books_list = Books.objects.all()
    if query:
        books_list = books_list.filter(Q(title__icontains=query))
    
    query = request.GET.get('category')
    books_list = Books.objects.all()
    if query:
        books_list = books_list.filter(Q(category__icontains=query))

    paginator = Paginator(books_list,10)
    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    context = {
        "books": post,
        "results":len(Books.objects.all())
    }
    return render(request, 'pages/index.html',context)

def view(request):
    return render(request,'pages/view.html',{})