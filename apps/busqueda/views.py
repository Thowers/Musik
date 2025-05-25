import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from django.conf import settings
from django.shortcuts import render

def buscador(request):
    artista = None
    albums = []
    error = None
    if request.method == 'POST':
        nombre = request.POST.get('artista', '').strip()
        if not nombre:
            error = 'Por favor ingresa un nombre de artista.'
        else:
            sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
                client_id=settings.SPOTIFY_CLIENT_ID,
                client_secret=settings.SPOTIFY_CLIENT_SECRET
            ))
            resultados = sp.search(q=nombre, type='artist', limit=1)
            if resultados['artists']['items']:
                artista_info = resultados['artists']['items'][0]
                artista = {
                    'name': artista_info['name'],
                    'images': artista_info['images'],
                    'popularity': artista_info['popularity'],
                    'genres': artista_info['genres'],
                }
                albums_sp = []
                results = sp.artist_albums(artista_info['id'], album_type='album')
                albums_sp.extend(results['items'])
                while results['next']:
                    results = sp.next(results)
                    albums_sp.extend(results['items'])
                for album in albums_sp:
                    tracks = sp.album_tracks(album['id'])
                    track_list = []
                    for track in tracks['items']:
                        track_list.append({
                            'name': track['name'],
                            'external_urls': track['external_urls']
                        })
                    albums.append({
                        'id': album['id'],
                        'name': album['name'],
                        'images': album['images'],
                        'tracks': track_list
                    })
            else:
                error = 'No se encontró el artista.'
    return render(request, 'pages/buscador.html', {'artista': artista, 'albums': albums, 'error': error})

