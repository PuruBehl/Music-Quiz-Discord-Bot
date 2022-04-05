from youtube_search import YoutubeSearch
import webbrowser

def return_song_url(song_name):

    results = YoutubeSearch(song_name, max_results=10).to_dict()
    
    return 'https://www.youtube.com' + results[0]["url_suffix"]