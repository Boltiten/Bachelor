import os
import pandas as pd
import sys
#The languages being used, these languages are folder names of downloaded podcasts
LANGUAGES = ["nor","eng","de"]
#Folder containing podcasts
LOCATION=sys.argv[1]

currentfile = os.path.dirname(os.path.abspath(__file__))
currentfile = currentfile.replace("\\","/")
audioDifLoc = currentfile.replace("/scripts","/podcasts")

#Read csv to speed up process if stopped halfway
try:
    data = pd.read_csv('adBreakpoints.csv',header=None,encoding='cp1252',sep="|").fillna
    data = data[0].str.split('|')[0]
    csvList = data.iloc[:, 0]
    csvList = csvList.values.tolist()
except:
    csvList=[]
for path, subdir, files in os.walk(LOCATION):
    for name in files:
        fullName = os.path.join(path,name)
        fullName = fullName.replace("\\","/")
        found = False
        foundLang = ""
        for lang in LANGUAGES:
             if lang+"/" in fullName:
                found = True
                foundLang = lang
                foundLangSlash = lang+"/"
        #Iterates through language folder if found
        if (found):
            fullName = foundLangSlash + fullName.split(foundLangSlash)[1]
            fullName = fullName.replace("\\","/")
            if (not fullName in csvList):
                Tor = fullName.replace("-"+foundLang+"-","-tor-").replace(foundLangSlash,"tor/")
                Tor = Tor.replace("-"+foundLang+"-","-tor-")
                Tor = LOCATION+ "/" + Tor
                fullName = LOCATION+ "/" + fullName
                print('python3 '+currentfile+ '/AudioDiff.py "' + Tor +'" "'+ fullName+'" "'+LOCATION+'"')
                os.system('python3 '+currentfile+ '/AudioDiff.py "' + Tor +'" "'+ fullName+'" "'+LOCATION+'"')
