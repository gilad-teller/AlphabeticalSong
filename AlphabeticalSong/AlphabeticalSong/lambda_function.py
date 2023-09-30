import json
import lib

def lambda_handler(event, context):
    params = event['multiValueQueryStringParameters']
    artists = []
    if type(params) is dict and 'artist' in params:
        artists = params['artist']
    song_url = lib.get_random_song_url(artists)
    ordered_lyrics = lib.get_ordered_lyrics(song_url)
    res = {
        'Artists': artists,
        'OrderedLyrics': ordered_lyrics,
        'Link': song_url
    }
    return {
        'statusCode': 200,
        'body': json.dumps(res, ensure_ascii=False).encode('utf8'),
        'headers': {
            'Access-Control-Allow-Origin': '*'
        }
    }