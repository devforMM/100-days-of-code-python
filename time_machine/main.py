import requests
from  bs4 import BeautifulSoup
import requests
import pprint

#----------------------------- website content-----------------------------------#
date=input("wich year to travel to ? type the date in this format yyyyy-mm-dd: ")
link=f"https://www.billboard.com/charts/hot-100/{date}/"
response=requests.get(link)
content=response.text
#------------------------------ extrating songs-----------------------------------#
soup=BeautifulSoup(content,"html.parser")
songs=soup.findAll(name="li", class_="o-chart-results-list__item")
titres=[]
for song in songs:
    if song.find(name="h3",id="title-of-a-story")!=None:
        titres.append(song.h3.text.strip())
#----------------------------- spotify ----------------------------------------------#
import spotipy
from spotipy.oauth2 import SpotifyOAuth
client_id="63706eeb33384bb0a7c1e978fe7b73ca"
Client_secret="1db7bd5201a8413fa961d2e2eaa06ce2"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=Client_secret,redirect_uri="https://example.com/",scope="playlist-modify-private" ))

user=sp.current_user()
user_id=user["id"]


uris=[]
for titre in titres:

 results=sp.search(q=titre,type="track",limit=1)
 uri=results["tracks"]["items"][0]["uri"]
 uris.append(uri)
 


ma_playlist=sp.user_playlist_create(user=user_id,public=False,description="top 100 songs ",name=f"playslist of {date}")

sp.user_playlist_add_tracks(user=user_id,playlist_id=ma_playlist["id"],tracks=uris,position=0)