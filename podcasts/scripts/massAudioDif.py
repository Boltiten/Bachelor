import os
import pandas as pd
LANGUAGES = ["nor","eng","de"]
try:
    data = pd.read_csv('adBreakpoints.csv',header=None,encoding='cp1252',sep="|").fillna
    data = data[0].str.split('|')[0]
    csvList = data.iloc[:, 0]
    csvList = csvList.values.tolist()
except:
    csvList=[]
os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.chdir("..")
os.chdir("podcasts")
for path, subdir, files in os.walk(os.getcwd()):
    for name in files:
        fullName = os.path.join(path,name)
        fullName = fullName.replace("\\","/")
        found = False
        foundLang = ""
        for lang in LANGUAGES:
             if lang+"/" in fullName:
                found = True
                foundLang = lang
                foundLangslash = lang+"/"
        if (found):
            fullName = foundLangslash + fullName.split(foundLangslash)[1]
            fullName = fullName.replace("\\","/")
            if (not fullName in csvList):
                Tor = fullName.replace("-"+foundLang+"-","-tor-").replace(foundLangslash,"tor/")
                Tor = Tor.replace("-"+foundLang+"-","-tor-")
                print('python AudioDiff.py "' + Tor +'" "'+ fullName+'"')
                os.system('python AudioDiff.py "' + Tor +'" "'+ fullName+'"')

    