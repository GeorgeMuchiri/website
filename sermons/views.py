from django.shortcuts import render

from sermons.models import Teacher, Sermon, Category


def index(request):
    marriage = Sermon.objects.filter(category__name="Pillars of Marriage").order_by("-date_created")[:1]
    foundation = Sermon.objects.filter(category__name="Foundation Class").order_by("-date_created")[:1]
    wisdom = Sermon.objects.filter(category__name="Pillars of Wisdom").order_by("-date_created")[:1]

    context  = {
    'marriage': marriage,
    'foundation': foundation,
    'wisdom': wisdom,
     }

    return render(request, 'sermons/index.html', context)


def about(request):
    return render(request, 'sermons/about.html')

def sermons(request):

    marriage = Sermon.objects.filter(category__name="Pillars of Marriage").order_by("-date_created")
    foundation = Sermon.objects.filter(category__name="Foundation Class").order_by("-date_created")
    wisdom = Sermon.objects.filter(category__name="Pillars of Wisdom").order_by("-date_created")
    context  = {
    'marriage': marriage,
    'foundation': foundation,
    'wisdom': wisdom,
     }
    return render(request, 'sermons/sermons.html', context)

def contact(request):
    return render(request, 'sermons/contact.html')
