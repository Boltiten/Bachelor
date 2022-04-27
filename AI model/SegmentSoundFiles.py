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
directory = 'D:/Podcasts/ad'

for podcast in os.listdir(directory):
    song_pieces = prepare_song(directory + '/' + podcast)
    all_tracks += song_pieces
    adBinary += ([1]*len(song_pieces))
    print(f"Finished: {podcast}")

directory = 'D:/Podcasts/noad'
for podcast in os.listdir(directory):
    song_pieces = prepare_song(directory + '/' + podcast)
    all_tracks += song_pieces
    adBinary += ([0]*len(song_pieces))
    print(f"Finished: {podcast}")

#TODO 
#Store segmentations in a file, so we can read it to the model later

np.save('podcast_segmented',podcast)
podcast_segmented = np.load('podcast_segmented')

if(podcast == podcast_segmented):
    print("Equal")
else:
    print("NOT Equal")

np.save('adBinary_segmented',adBinary)
adBinary_segmented = np.load('adBinary_segmented')
