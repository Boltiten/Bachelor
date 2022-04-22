import sys
import re
import csv
import pathlib
import os

LOCATION="/media/morten/T7/Podcasts/"

adfile = open(sys.argv[2], 'rb').read()
noadfile = open(sys.argv[1], 'rb').read()

print("Adfile: {} {} bytes".format(sys.argv[2],len(adfile)))
print("Non adfile: {} {} bytes".format(sys.argv[1],len(noadfile)))

print("-"*40)
try:
    assert(len(adfile) > len(noadfile))
except:
    quit()

adadvance = 0
noadadvance = 0
adindex = 1
diffarr=[]

path = pathlib.PurePath(sys.argv[2])
path.parent.name +","+ path.name
fileString = path.parent.name +"/"+ path.name
diffarr.append(fileString)
diffarr.append(0)
while True:
    xor = bytes(a ^ b for a, b in zip(adfile[adadvance:], noadfile[noadadvance:]))
    print(str(noadadvance)+" "+str(adadvance))
    matches = re.match(b'[\x00]*', xor)
    advance = matches.end()

    # Stop if we're at the end of the adfile
    if advance + adadvance >= len(adfile) or advance + noadadvance >= len(noadfile):
        break
    diffarr.append(adadvance+advance)
    print("Diff at {} in {} from {} in {}".format(advance + adadvance,sys.argv[2], advance + noadadvance, sys.argv[1]))

    adbegin = advance + adadvance
    print("begin ad {}: {}".format(sys.argv[2], advance + adadvance))

    print("search offset {} {} bytes".format(sys.argv[1], advance + noadadvance))

    # Search for the next 512? bytes from noadfile in adfile
    search = noadfile[advance + noadadvance:advance + noadadvance + 512]

    print(search[0:16])
    searchin = adfile[adadvance:]
    adadvancePre = adadvance
    try:
        adadvance = adadvance+searchin.index(search)
    except:
        diffarr.append(len(adfile)-1)
        break
    if(adadvance<adadvancePre+advance):
        diffarr.append(len(adfile)-1)
        print("EOF")
        break
    diffarr.append(adadvance)
    print("end ad {}: {}".format(sys.argv[2], adadvance))
    noadadvance += advance

    print("-"*20)
csvFile = open(LOCATION+'adBreakpoints.csv','a', newline="")
csvWriter = csv.writer(csvFile, delimiter="|")
csvWriter.writerow(diffarr)
csvFile.close()

if (not os.path.exists("ad")):
    os.makedirs("ad")
    os.makedirs("noad")

fileCount = 0
fileNameString = path.parent.name +","+ path.name
for i in range(1,len(diffarr)-1):
    if (i%2==0):
        folder = "ad/"
    else: folder = "noad/"
            
    file = open(LOCATION+folder+str(fileCount)+fileNameString,"wb")
    file.write(adfile[diffarr[i]:diffarr[i+1]])
    print("FILENAMESTRING: "+folder+str(fileCount)+fileNameString)
    file.close
    fileCount = fileCount+1
print("Done.")

#For generating unique name for podcasts
def getFileName(filePath,delimeter):
    path = pathlib.PurePath(filePath)
    return path.parent.name +delimeter+ path.name

def splitAudio(segmentBitLength,startpos,endpos,filenameString,oddMeansAd):
    global fileCount
    if (oddMeansAd%2==1):
        if (not os.path.exists("ad")):
            os.makedirs("ad")
        folder = "ad/"
    else:
        if (not os.path.exists("noad")):
            os.makedirs("noad")
        folder = "noad/"
    for i in range((int)((endpos-startpos)/segmentBitLength)):
        file = open(LOCATION+folder+str(fileCount)+filenameString,"wb")
        fileCount = fileCount+1
        pos=startpos+i*segmentBitLength
        file.write(adfile[pos:pos+segmentBitLength])
        print("FILENAMESTRING: "+folder+str(fileCount)+filenameString)
        file.close()
