from django.shortcuts import render
from .forms import ContactForm, MessagesForm
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
    serms = Sermon.objects.all()
    context  = {
    'marriage': marriage,
    'foundation': foundation,
    'wisdom': wisdom,
    'serms': serms
     }
    return render(request, 'sermons/sermons.html', context)

def contact(request):
    form = MessagesForm()
    if request.method == 'POST':
        form = MessagesForm(request.POST or None)
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        if form.is_valid():
            form.save()
            form = MessagesForm()
    context = {
    'form': form
    }
    return render(request, 'sermons/contact.html', context)


def categories(request):
    cat = Category.objects.all()
    context = {
    'cat': cat
    }
    return render(request, 'sermons/category.html', context)

def foundation(request):
    foundation = Sermon.objects.filter(category__name="Foundation Class").order_by("-date_created")
    context = {
    'foundation': foundation
    }
    return render(request, 'sermons/found.html', context)

def marriage(request):
    marriage = Sermon.objects.filter(category__name="Pillars of Marriage").order_by("-date_created")
    context = {
    'marriage': marriage
    }
    return render(request, 'sermons/marriage.html', context)

def wisdom(request):
    wisdom = Sermon.objects.filter(category__name="Pillars of Wisdom").order_by("-date_created")
    context = {
    'wisdom': wisdom
    }
    return render(request, 'sermons/wisdom.html', context)
