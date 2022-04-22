from pathlib import Path, PurePath
import subprocess
import os
LOCATION="/media/morten/T7/Podcasts"
rootdir=Path(LOCATION)
#rootdir = Path(__file__).parent.parent.absolute() / "podcasts"
file_list = [f for f in rootdir.resolve().glob('**/*') if f.is_file()]
for file in file_list:
    name, ext = file.name.rsplit(".",1)
    if ext == "mp3" and (file.parent.name=="ad" or file.parent.name == "noad") and not os.path.exists(LOCATION+"/"+file.parent.name+"/"+name.replace(" ","")+".wav"):
        #if name[0] == "-":
            #print(file.parent.name)
            #file.rename(file.parent.name+ "/"+ file.name.replace("-","",1))
        print(LOCATION+"/"+file.parent.name+"/"+name.replace(" ","")+".wav")
        try:
            subprocess.call(['ffmpeg', '-i',file.resolve(), LOCATION+"/"+file.parent.name+"/"+name.replace(" ","")+".wav"])
        except:
            print("error handling file")
