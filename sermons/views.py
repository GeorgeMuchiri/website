from django.shortcuts import render

from sermons.models import Teacher, Sermon, Category


def index(request):
    p = Sermon.objects.all()
    context = {'teacher': p}
    return render(request, 'sermons/index.html', context)


def about(request):
    return render(request, 'sermons/about.html')

def sermons(request):
    posts = Sermon.objects.filter(category__name='Pillars of Marriage')
    context  = {
    'posts': posts
     }
    return render(request, 'sermons/sermons.html', context)

def contact(request):
    return render(request, 'sermons/contact.html')
