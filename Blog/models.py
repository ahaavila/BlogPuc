from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class PostQuerySet(models.QuerySet):
    def publicados(self):
        return self.filter(publicado=True)

class Comentario (models.Model):
    post = models.ForeignKey('Post')
    autor = models.CharField (max_length=100)
    texto = models.TextField()
    likes = models.IntegerField (default=0)
    unlikes = models.IntegerField(default=0)
    data_criado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str (self.post) + " - " + self.autor + " - " + self.data_criado.strftime('%Y/%m/%d - %H:%M')

    def like (self):
        self.likes += 1

    def unlike (self):
        self.unlikes += 1

class Post (models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    publicado = models.BooleanField(default=True)
    data_criado = models.DateTimeField(auto_now_add=True)
    data_modificado = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True)

    objects = PostQuerySet.as_manager()
    
    def get_absolute_url(self):
        return ("post_detail", (), {"id": self.id})
    
    def __str__(self):
        return self.titulo
