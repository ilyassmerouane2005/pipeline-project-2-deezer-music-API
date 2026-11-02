import requests 
import json
base_url = 'https://api.deezer.com/chart'
response = requests.get(base_url).json()
response_sections = response.keys()
print('The sections in the response are:', response_sections)
print('=' * 50)

response_tracks_sections = response['tracks'].keys()
print('The sections in the tracks response are:', response_tracks_sections)
response_tracks_sections_data = response['tracks']['data'][0].keys()
print('The sections in the tracks data response are:', response_tracks_sections_data) 
response_tracks_sections_total = response['tracks']['total']
print( 'The total number of tracks in the response is:', response_tracks_sections_total)
print('=' * 50)

response_albums_sections = response['albums'].keys()
print('The sections in the albums response are:', response_albums_sections)
response_albums_sections_data = response['albums']['data'][0].keys()
print('The sections in the albums data response are:', response_albums_sections_data) 
response_albums_sections_total = response['albums']['total']
print( 'The total number of albums in the response is:', response_albums_sections_total)
print('=' * 50)

response_artists_sections = response['artists'].keys()
print('The sections in the artists response are:', response_artists_sections)
response_artists_sections_data = response['artists']['data'][0].keys()
print('The sections in the artists data response are:', response_artists_sections_data)
response_artists_sections_total = response['artists']['total']
print( 'The total number of artists in the response is:', response_artists_sections_total)
print('=' * 50)

response_playlists_sections = response['playlists'].keys()
print('The sections in the playlists response are:', response_playlists_sections)
response_playlists_sections_data = response['playlists']['data'][0].keys()
print('The sections in the playlists data response are:', response_playlists_sections_data)
response_playlists_sections_total = response['playlists']['total']
print( 'The total number of playlists in the response is:', response_playlists_sections_total)
print('=' * 50)

response_podcasts_sections = response['podcasts'].keys()
print('The sections in the podcasts response are:', response_podcasts_sections)
response_podcasts_sections_data = response['podcasts']['data'][0].keys() 
print('The sections in the podcasts data response are:', response_podcasts_sections_data)
response_podcasts_sections_total = response['podcasts']['total']
print( 'The total number of podcasts in the response is:', response_podcasts_sections_total)

"""
this api has 5 big sections every section has 10 rows :
section 1) tracks : we will create a dataframe with the columns : id , title , link , duration , rank , preview , (from artist we will select name) , type 
section 4) playlists : we will create a dataframe with the columns : id , title , public , nb_tracks , link , picture , creation_date , tracklist , type
"""