from django.shortcuts import render

from Blog.models import Post, Categoria

# Create your views here.

def blog(request):

    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"post": posts})

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render (request, "blog/categoria.html", {'categoria':categoria, "post": posts})