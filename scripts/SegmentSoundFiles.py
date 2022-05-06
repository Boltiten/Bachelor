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
    skip = 5000
    while start + skip < end:
        song_pieces.append(song[start:start+skip])
        start += skip
    return song_pieces

def prepare_song(song_path):
    list_matrices = []
    y,sr = librosa.load(song_path,sr=22050)
    song_pieces = cut_song(y)
    for song_piece in song_pieces:
        melspec = librosa.feature.melspectrogram(song_piece)
        list_matrices.append(melspec)
    return list_matrices


"""
all_podcasts = []
adBinary = []
directory = 'E:/Podcasts/ad'

for podcast_name in os.listdir(directory):
    podcast = prepare_song(directory + '/' + podcast_name)
    all_podcasts += podcast
    adBinary += ([1]*len(podcast))
    print(f"Finished: {podcast_name}")
"""
directory = 'E:/Podcasts/noad_vicegaming'
for podcast_name in os.listdir(directory):
    podcast = prepare_song(directory + '/' + podcast_name)
    all_podcasts += podcast
    adBinary += ([0]*len(podcast))
    print(f"Finished: {podcast_name}")

print(" ")

np.save('AI/podcast_segmented.npy',all_podcasts)
podcasts_segmented = np.load('AI/vicegaming_test_x_segmented.npy')

np.save('AI/adBinary_segmented.npy',adBinary)
adBinary_segmented = np.load('AI/vicegaming_test_y_segmented.npy')


print((all_podcasts==podcasts_segmented).all())