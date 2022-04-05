from spotify import *
from youtube_url import *
import random

def combined_spotify_youtube(playlist_link) :
    names,authors = playlist_details(playlist_link)
    n2=[]
    a2=[]
    number_of_songs=10
    names=names[:number_of_songs]
    authors = authors[:number_of_songs]
    youtube_links=[]
    for i,j in zip(names,authors) :
        try :
            youtube_links.append(return_song_url(i.replace(" ",".")+".by."+j.replace(" ",".")))
            n2.append(i)
            a2.append(j)
        except :
            pass


    return youtube_links,n2,a2