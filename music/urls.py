#including the include functioanlity to show views of other apps
from django.conf.urls import include, url
from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.index, name="index"),

    # /music/pata
    path('pata/', views.pata, name="pata"),

    # /music/1/
    path('<album_id>/', views.detail, name="detail"),

    # /music/1/favorite
    path('<album_id>/favorite', views.favorite, name="favorite"),


]
