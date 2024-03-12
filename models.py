from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    nombreB=models.CharField(max_length=50) 
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombreB
    
class Post(models.Model):
    titulo=models.CharField(max_length=500)
    contenido=models.CharField(max_length=10000)
    imagen=models.ImageField(upload_to='Blog', null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=Categoria.nombreB="trippy stories"
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)

    class meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo