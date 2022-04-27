from IPython.display import Audio
import librosa
import os
import numpy as np
import warnings
warnings.simplefilter('ignore')

def cut_song(song):
    start = 0
    end = len(song)
    song_pieces = []
    while start + 10000 < end:
        song_pieces.append(song[start:start+10000])
        start += 10000
    return song_pieces

def prepare_song(song_path):
    list_matrices = []
    y,sr = librosa.load(song_path,sr=22050)
    song_pieces = cut_song(y)
    for song_piece in song_pieces:
        melspec = librosa.feature.melspectrogram(song_piece)
        list_matrices.append(melspec)
    return list_matrices



all_tracks = []
adBinary = []
directory = 'D:/Podcasts/adsmall'

for podcast_name in os.listdir(directory):
    podcasts = prepare_song(directory + '/' + podcast_name)
    all_tracks += podcasts
    adBinary += ([1]*len(podcasts))
    print(f"Finished: {podcast_name}")

directory = 'D:/Podcasts/noadsmall'
for podcast_name in os.listdir(directory):
    podcasts = prepare_song(directory + '/' + podcast_name)
    all_tracks += podcasts
    adBinary += ([0]*len(podcasts))
    print(f"Finished: {podcast_name}")

print(" ")

np.save('podcast_segmented.npy',podcasts)
podcasts_segmented = np.load('podcast_segmented.npy')

np.save('adBinary_segmented.npy',adBinary)
adBinary_segmented = np.load('adBinary_segmented.npy')


print((podcasts==podcasts_segmented).all())