import os
from pydub import AudioSegment

audio_files = os.listdir()

for file in audio_files:
    name, ext = os.path.splitext(file)
    if ext == ".mp3":
       mp3_sound = AudioSegment.from_mp3(file)
       mp3_sound.export("{0}.wav".format(name), format="wav")