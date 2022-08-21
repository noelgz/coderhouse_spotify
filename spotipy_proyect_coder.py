import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import pandas as pd
import boto3
from botocore.exceptions import ClientError

import os
import json
import psycopg2
from sqlalchemy import create_engine


_SPOTIFY_USER_ID = 'noel.argonzalez'
_EXPORT_FILENAME = 'spotify_features_songs_cleaned.csv'

def getAccessKeys(service):
    """Get the access keys of the services to use

    Args:
        service (str): Service to connect

    Returns:
        json: Return the connection string
    """
    json_file = open('secrets_key.json')
    json_data = json.load(json_file)

    return json_data[service]


def createSpotifyConnection():
    """Create connection to Spotify

    Returns:
        Client.Spotify: Return the connection object to Spotify
    """
    spotify_secret = getAccessKeys('spotify_keys')
    client_credentials_manager = SpotifyClientCredentials(
                                        client_id = spotify_secret['client_id'], 
                                        client_secret = spotify_secret['client_secret']
                                 )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    return sp


def getPlaylistIDUser(sp, user):
    """Get all the user's playlists

    Args:
        sp (Client.Spotify): The connection object to Spotify
        user (str): Spotify user

    Returns:
        list: Returns a list with all the urls of the playlists
    """
    playlist_user = []
    playlists = sp.user_playlists(user)
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            playlist_user.append(playlist['uri'])

        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None
        
        return playlist_user


def getTrackIDs(sp, user, playlist_id):
    """Get all the songs of the received playlist sent by parameter

    Args:
        sp (Client.Spotify): The connection object to Spotify
        user (str): Spotify user
        playlist_id (str): Playlist ID

    Returns:
        list: Returns a list with the ids of the songs of the playlist
    """
    ids = []
    playlist = sp.user_playlist(user, playlist_id)

    for item in playlist['tracks']['items']:
        track = item['track']

        try:
          ids.append(track['id'])
        except:
          pass

    return ids


def getTrackFeatures(sp, id):
    """Get the metadata of the songs

    Args:
        sp (Client.Spotify): The connection object to Spotify
        id (str): Song ID

    Returns:
        list: Returns a list with all the metadata of the song sent by parameter
    """
    meta = sp.track(id)
    features = sp.audio_features(id)

    # meta
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    release_date = meta['album']['release_date']
    length = meta['duration_ms']
    popularity = meta['popularity']

    # features
    acousticness = features[0]['acousticness']
    danceability = features[0]['danceability']
    energy = features[0]['energy']
    instrumentalness = features[0]['instrumentalness']
    loudness = features[0]['loudness']
    tempo = features[0]['tempo']
    time_signature = features[0]['time_signature']
    key = features[0]['key']
    mode = features[0]['mode']
    uri = features[0]['uri']

    #genre
    genre_artist = sp.search(artist, type='artist')
    genre = None

    try:
      genre = genre_artist['artists']['items'][0]['genres']
    except:
      pass

    track = [name, album, artist, genre, release_date, length, popularity, 
             acousticness, danceability, energy, instrumentalness, loudness, 
             tempo, time_signature, key, mode, uri]

    return track


def getFeaturesSongForPlaylist(sp, playlist_ids):
    """Loop through the playlist and each song and get the metadata for each

    Args:
        sp (Client.Spotify): The connection object to Spotify
        playlist_ids (list): List of user playlists

    Returns:
        list: Returns a list with all the songs in the playlists and their metadata
    """
    playlist_ids = ['spotify:playlist:0VJgMncIqQcYn7H5cgg2Zu']
    tracks = []
    for i in range(len(playlist_ids)):
      for j in range(len(getTrackIDs(sp, _SPOTIFY_USER_ID, playlist_ids[i]))):
        track = getTrackFeatures(sp, getTrackIDs(sp, _SPOTIFY_USER_ID, playlist_ids[i])[j])
        tracks.append(track)
    return tracks


def generateDataframe(data):
    """Generate a dataframe with the extracted data

    Args:
        data (list): Data extracted from Spotify API

    Returns:
        Object: Return a Pandas dataframe
    """
    df = pd.DataFrame(data, columns = ['name', 'album', 'artist', 'genre', 'release_date',
                                       'length', 'popularity', 'acousticness', 'danceability',
                                       'energy', 'instrumentalness', 'loudness',
                                       'tempo', 'time_signature', 'key', 'mode', 'uri'])
    return df


def createS3Connection():
    """Create the connection to the AWS service

    Returns:
        S3.client: S3 connection object
    """
    aws_conection = getAccessKeys('secret_aws')
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_conection['aws_access_key_id'],
        aws_secret_access_key=aws_conection['aws_secret_access_key'],
        aws_session_token=aws_conection['aws_session_token']
    )

    return s3


def creatingBucket(s3):
    """Create a bucket in AWS

    Args:
        s3 (S3.client): S3 connection object
    """

    try:
        response = s3.create_bucket(
        ACL='private',
        Bucket='tp-coderhouse'
        )
        print('The bucket has been created!')
    except Exception as e:
        print(e)


def upload_file(s3_client, file_name, bucket, object_name=None):
    """Upload a file to the AWS S3 service

    Args:
        s3_client (S3.client): S3 connection object
        file_name (str): Name of the file to upload
        bucket (str): File destination bucket name
        object_name (str, optional): URL of the file to upload to the S3 bucket. Defaults to None.

    Returns:
        Boolean: Returns True on successful connection or False on failed connection
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        print(e)
        return False
    return True

def _extract(sp):
    """Get the songs and their metadata from all the user's playlists

    Args:
        sp (Client.Spotify): The connection object to Spotify

    Returns:
        list: Returns a list with the metadata of all songs
    """
    playlists_data = getPlaylistIDUser(sp, _SPOTIFY_USER_ID)
    payload = getFeaturesSongForPlaylist(sp, playlists_data)
    
    return payload


def _transform(df):
    """The RAP genre is added to all the songs where the artist will be "Sindicato" and have the genre in NULL

    Args:
        df (Object): Get the created pandas dataframe

    Returns:
        Object: Return a new dataset with the clean data
    """
    df['genre2'] = df['genre'].str[-1]    
    df.loc[(df['genre2'].isnull()) & (df['artist'].str.contains('Sindicato', na=False)), 'genre'] = 'rap'
    df['genre'] = df['genre'].str[-1]
    del(df['genre2'])
    df_cleaned = df[~df['genre'].isnull()]

    return df_cleaned


def _load(service, df=None, s3=None):
    """Get the data to upload in the S3 services or database

    Args:
        service (str): Service to upload the data
        df (Object, optional): Pandas dataframe to upload the data to the database. Defaults to None.
        s3 (S3.client: S3 connection object, optional): S3 connection object. Defaults to None.
    """
    db_credentials = getAccessKeys('secret_postgresql')
    

    if service == 'database':

        try:
            
            conn = psycopg2.connect(
                host = db_credentials['host'],
                database = db_credentials['database'],
                user = db_credentials['user'],
                password = db_credentials['passw'],
                port = db_credentials['port']
            )
            print("Connection succesfully to " + db_credentials['database'])

        except Exception as error:
            print(error)
        

        try:

            cur = conn.cursor()
            conn_string = f'postgresql://postgres:admin@127.0.0.1/coderhouse'
            db = create_engine(conn_string)
            conndb = db.connect()

            df.to_sql('spotify_coderhouse', conndb, if_exists='append', index=False)
            print('The data has been uploaded to PostgreSQL!')

        except Exception as error:
            print(error)

        conn.commit()
        conn.close()
        cur.close()

    elif service == 'S3':

        creatingBucket(s3)
        upload_file(s3, _EXPORT_FILENAME, 'tp-coderhouse')
        print('The CSV File has been uploaded to S3!')

    else:
        print('Enter a correct option.')


if __name__ == '__main__':
    sp = createSpotifyConnection()
    s3 = createS3Connection()
    
    # Data extract
    print('Starting the data extraction process . . . ')
    data = _extract(sp)
    df = generateDataframe(data)

    # Data Transform
    print('\nStarting the data transformation process . . .')
    df_clean = _transform(df)
    df_clean.to_csv(_EXPORT_FILENAME, index=False)

    # Data Load
    print('\nStarting the data load process . . .')
    _load('database', df_clean)
    _load('S3', None, s3)



