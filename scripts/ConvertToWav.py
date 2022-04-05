from pathlib import Path
import subprocess
rootdir = Path(__file__).parent.parent.absolute() / "podcasts"
file_list = [f for f in rootdir.resolve().glob('**/*') if f.is_file()]
for file in file_list:
    name, ext = file.name.rsplit(".",1)
    if ext == "mp3" and (file.parent.name=="ad" or file.parent.name == "noad"):
        if name[0] == "-":
            print(file.parent.name)
            file.rename(file.parent.name+ "/"+ file.name.replace("-","",1))
        subprocess.call(['ffmpeg', '-i',name+".mp3", name.replace(" ","")+".wav"])