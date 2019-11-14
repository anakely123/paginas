from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post 
from django.urls import reverse_lazy

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('listagem')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['titulo', 'texto']

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['titulo', 'autor', 'texto']


class PostagemDetailView(DetailView): 
    model = Post
    template_name = 'post_detail.html'

class ListagemView(ListView):
    model = Post
    template_name = 'listagem.html'
    context_object_name = 'lista'