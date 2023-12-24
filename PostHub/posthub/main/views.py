from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .models import dnld
from .forms import dnldForm
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

class PostView(View):
    '''Главная страница'''
    '''вывод записей для главной страницы'''
    def get(self, request):
        posts = dnld.objects.order_by('-id')
        return render(request, 'main/home.html', {'post_list': posts})


class PostDetail(View):
    '''Страниуа item'''
    '''отдельная страница для каждой статьи'''
    def get(self, request, pk):
        post = dnld.objects.get(id=pk)
        return render(request, 'main/item.html', {'post': post})


def create(request):
    error = ''
    if request.method == 'POST':
        form = dnldForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.created_at = datetime.now()
            article.author = request.user
            article.save()
            return redirect('home')
        else:
            error = form.errors.as_ul()
    form = dnldForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


class UserPostListView(ListView):
    model = dnld
    template_name = 'user/prof.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))

        return dnld.objects.filter(author=user).order_by('-date_posted')


