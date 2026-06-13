from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404

from news.forms import RegisterForm, NewsForm
from .models import News
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


def home(request):
    query = request.GET.get('q')

    if query:
        news = News.objects.filter(title__icontains=query)
    else:
        news = News.objects.all().order_by('-created_at')

    latest_news = News.objects.all().order_by('-created_at')

    return render(request, 'home.html', {
        'news': news,
        'latest_news': latest_news
    })
def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)

    news.views += 1
    news.save()

    return render(request, 'detail.html', {
        'news': news
    })
def category_news(request, category):
    news = News.objects.filter(category=category)

    latest_news = News.objects.all().order_by('-created_at')

    return render(request, 'home.html', {
        'news': news,
        'latest_news': latest_news
    })

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Registraciya múvaffaqiyatlı tamamlandı!"
            )

            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {
        'form': form
    })
@staff_member_required
def dashboard(request):
    news = News.objects.all().order_by('-created_at')

    return render(request, 'dashboard.html', {
        'news': news
    })
@staff_member_required
def dashboard(request):
    news = News.objects.all().order_by('-created_at')

    return render(request, 'dashboard.html', {
        'news': news
    })


@staff_member_required
def news_create(request):

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = NewsForm()

    return render(request, 'news_form.html', {
        'form': form,
        'title': 'Jańalıq qosıw'
    })


@staff_member_required
def news_edit(request, pk):

    news = get_object_or_404(News, pk=pk)

    if request.method == 'POST':
        form = NewsForm(
            request.POST,
            request.FILES,
            instance=news
        )

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = NewsForm(instance=news)

    return render(request, 'news_form.html', {
        'form': form,
        'title': 'Jańalıqtı ózgertiw'
    })


@staff_member_required
def news_delete(request, pk):

    news = get_object_or_404(News, pk=pk)

    news.delete()

    return redirect('dashboard')