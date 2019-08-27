from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^post/(?P<pk>[0-9]+)$', views.BlogDetail.as_view(), name="post"),
    url(r'^post/(?P<pk>[0-9]+)/comentario$', views.comentario_novo, name="comentario_novo"),
    url(r'^comentario/(?P<pk>[0-9]+)/like$', views.comentario_like, name="comentario_like"),
    url(r'^comentario/(?P<pk>[0-9]+)/unlike$', views.comentario_unlike, name="comentario_unlike"),

]