from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import ComentarioForm
from .models import Post, Comentario

# Create your views here.
class BlogIndex (ListView):
    queryset = Post.objects.publicados ()
    template_name = 'home.html'
    paginate_by = 3

class BlogDetail (DetailView):
    model = Post
    template_name = 'post.html'

def comentario_novo(request, pk):
    post = get_object_or_404 (Post, pk=pk)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            comentario.save()
            return redirect (reverse ('post', kwargs={'pk': post.pk}))
    else:
        form = ComentarioForm()
    return render (request, 'comentario.html', {'form': form})

def comentario_like(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    comentario.like()
    comentario.save()
    return redirect (reverse ('post', kwargs={'pk': comentario.post_id}))

def comentario_unlike(request, pk):
    comentario = get_object_or_404(Comentario, pk=pk)
    comentario.unlike()
    comentario.save()
    return redirect(reverse('post', kwargs={'pk': comentario.post_id}))