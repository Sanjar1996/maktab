from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .models import Articles


class BlogListView(ListView):
    model = Articles
    template_name = 'blog.html'


class BlogDetailView(DetailView):
    model = Articles
    template_name = 'blog-detail.html'


class BlogUpdateView(UpdateView):
    model = Articles
    fields = ('title', 'summary', 'body', 'photo')
    template_name = 'blog-edit.html'


class BlogDeleteView(DeleteView):
    model = Articles
    template_name = 'blog-delete.html'
    success_url = reverse_lazy('blog')


class BlogCreateView(CreateView):
    model = Articles
    fields = ('title', 'summary', 'body', 'photo', 'auth')
    template_name = 'blog-new.html'
