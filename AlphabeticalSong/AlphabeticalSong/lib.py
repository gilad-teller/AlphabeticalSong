import requests
import random
from bs4 import BeautifulSoup

def clean_up_word(word):
    return word.replace('\"', '').replace('\'', '').replace('.', '').replace(',', '').replace('-', '').replace('/', '').replace('\\', '').replace('(', '').replace(')', '')

def get_song_links(artist):
    artist_url = f'https://shironet.mako.co.il/artist?type=works&lang=1&prfid={artist}&class=4&sort=popular'
    print('Getting artist', artist_url)
    artist_html = requests.get(artist_url)
    artist_soup = BeautifulSoup(artist_html.text, 'html.parser')
    song_links = artist_soup.find_all('a', class_ = 'artist_player_songlist')
    return song_links

def get_random_song_url(artists):
    random.seed()
    song_links = []
    if len(artists) > 0:
        artist = random.choice(artists)
        song_links = get_song_links(artist)
    else:
        while len(song_links) < 1:
            artist = random.randrange(1, 9985)
            song_links = get_song_links(artist)
    song = random.choice(song_links)
    song_url = f'https://shironet.mako.co.il{song.attrs["href"]}'
    return song_url    

def get_ordered_lyrics(song_url):
    print('Getting song', song_url)
    song_html = requests.get(song_url)
    song_soup = BeautifulSoup(song_html.text, 'html.parser')
    song_lyrics_array = song_soup.find('span', class_ = 'artist_lyrics_text')
    words_array = song_lyrics_array.text.split()
    words_array.sort()
    ordered_song = ' '.join([clean_up_word(word) for word in words_array])
    return ordered_song