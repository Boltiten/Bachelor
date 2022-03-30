from IPython.display import Audio
import librosa

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
    y,sr = librosa(song_path,sr=22050)
    song_pieces = cut_song(y)
    for song_piece in song_pieces:
        melspec = librosa.feature.melspectrogram(song_piece)
        list_matrices.append(melspec)
    return list_matrices