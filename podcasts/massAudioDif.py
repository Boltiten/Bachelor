import os
import pandas as pd
LANGUAGES = ["nor","eng","de"]
try:
    data = pd.read_csv('adBreakpoints.csv', on_bad_lines='skip', sep="|",header=None)
    csvList = data.iloc[:, 0]
    csvList = csvList.values.tolist()
except:
    csvList=[]

for path, subdir, files in os.walk("C:/Users/Thomas/Downloads/podcasts"):
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
                print('python AudioDiff.py "' + Tor +'" "'+ fullName+'" '+ "50000")
                os.system('python AudioDiff.py "' + Tor +'" "'+ fullName+'" '+ "50000")
