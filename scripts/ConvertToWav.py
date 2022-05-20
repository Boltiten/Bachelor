from pathlib import Path
import subprocess
import os
import sys
#running example: python3 ConvertToWav.py "D:/Podcasts"
LOCATION=sys.argv[1]
rootdir=Path(LOCATION)
file_list = [f for f in rootdir.resolve().glob('**/*') if f.is_file()]
for file in file_list:
    name, ext = file.name.rsplit(".",1)
    #only converts in correctly labelled folders and checks whether allready converted
    if ext == "mp3" and (file.parent.name=="ad" or file.parent.name == "noad") and not os.path.exists(LOCATION+"/"+file.parent.name+"/"+name.replace(" ","")+".wav"):
        print(LOCATION+"/"+file.parent.name+"/"+name.replace(" ","")+".wav")
        try:
            subprocess.call(['ffmpeg', '-i',file.resolve(), LOCATION+"/"+file.parent.name+"/"+name.replace(" ","")+".wav"])
            os.remove(file)
        except:
            print("error handling file")
