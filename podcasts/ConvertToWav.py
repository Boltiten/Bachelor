from pathlib import Path
import subprocess

rootdir = Path("C:\\Users\\Thomas\\Downloads\\podcasts")
file_list = [f for f in rootdir.resolve().glob('**/*') if f.is_file()]
print(rootdir.name)
for file in file_list:
    print(file.name)
    name, ext = file.name.rsplit(".",1)
    if ext == "mp3":
        if name[0] == "-":
            print(file.parent.name)
            file.rename(file.parent.name+ "/"+ file.name.replace("-","",1))
        subprocess.call(['ffmpeg', '-i',name+".mp3", name.replace(" ","")+".wav"])
