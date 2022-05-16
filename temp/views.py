from django.shortcuts import render, redirect
from .models import Articles
from temp.models import Articles
from .forms import ArticlesForm


# def new_post(request):
#     posts = Articles.objects.all()
#     contex = {'posts': posts}
#     return render(request, 'index.html', context=contex)


def index(request):
    posts = Articles.objects.all()
    contex = {'posts': posts}
    return render(request, 'index.html', context=contex)
    # return render(request,
    #               template_name='index.html')


def agriculture(request):
    return render(
        request,
        template_name='Agriculture.html'
    )


def farmer(request):
    return render(request,
                  template_name='Farmer.html')


def fields(request):
    return render(request,
                  template_name='Fields.html')


def fruit(request):
    return render(request,
                  template_name='Fruit.html')


def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')

    form = ArticlesForm
    data = {
        'form': form,
    }
    return render(request, './create.html', data)


