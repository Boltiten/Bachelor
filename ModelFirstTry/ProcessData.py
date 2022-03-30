from IPython.display import Audio
import librosa
import os


def cut_song(song):
    start = 0
    end = len(song)
    song_pieces = []
    while start + 100000 < end:
        song_pieces.append(song[start:start+100000])
        start += 100000
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
genre = []
directory = 'C:\\Users\\Morten\\Desktop\\School\\Bachelor\\ModelFirstTry\\Tool\\ænima'

for song_name in os.listdir(directory):
    song_pieces = prepare_song(directory + song_name)
    all_tracks += song_pieces
    genre += ([0]*len(song_pieces))

directory = 'C:\\Users\\Morten\\Desktop\\School\\Bachelor\\ModelFirstTry\\Tool\\Lateralus'
for song_name in os.listdir(directory):
    song_pieces = prepare_song(directory + song_name)
    all_tracks += song_pieces
    genre += ([0]*len(song_pieces))