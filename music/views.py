from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


def pata(request):
    return render(request, 'music/pata.html', {'ok': 'ok'})


def detail(request, album_id):
    try:
        album = Album.objects.get(pk = album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")

    return render(request, 'music/details.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)

    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/details.html', {'album': album})
    else:
        selected_song.if_fvrt = True
        selected_song.save()

        return render(request, 'music/details.html', {'album': album})
