import sys
import re
import csv
import pathlib
import os

adfile = open(sys.argv[2], 'rb').read()
noadfile = open(sys.argv[1], 'rb').read()

print("Adfile: {} {} bytes".format(sys.argv[2],len(adfile)))
print("Non adfile: {} {} bytes".format(sys.argv[1],len(noadfile)))

print("-"*40)

assert(len(adfile) > len(noadfile))

adadvance = 0
noadadvance = 0
adindex = 1
diffarr=[]

path = pathlib.PurePath(sys.argv[2])
path.parent.name +","+ path.name
fileString = path.parent.name +"/"+ path.name
diffarr.append(fileString)
while True:
    xor = bytes(a ^ b for a, b in zip(adfile[adadvance:], noadfile[noadadvance:]))
    matches = re.match(b'[\x00]*', xor)
    advance = matches.end()

    # Stop if we're at the end of the adfile
    if advance + adadvance >= len(adfile) or advance + noadadvance >= len(noadfile):
        csvFile = open('adBreakpoints.csv','a', newline="")
        csvWriter = csv.writer(csvFile, delimiter="|")
        csvWriter.writerow(diffarr)
        csvFile.close()

        if (not os.path.exists("ad")):
            os.makedirs("ad")
            os.makedirs("noad")

        fileCount = 0
        fileNameString = path.parent.name +","+ path.name
        for i in range(1,len(diffarr)-1):
            if (i%2==1):
                folder = "ad/"
            else: folder = "noad/"
            
            file = open(folder+str(fileCount)+fileNameString,"wb")
            file.write(adfile[diffarr[i]:diffarr[i+1]])
            file.close
            fileCount = fileCount+1
        print("Done.")
        break
    diffarr.append(advance+adadvance)
    print("Diff at {} in {} from {} in {}".format(advance + adadvance,sys.argv[2], advance + noadadvance, sys.argv[1]))

    adbegin = advance + adadvance
    print("begin ad {}: {}".format(sys.argv[2], advance + adadvance))

    print("search offset {} {} bytes".format(sys.argv[1], advance + noadadvance))

    # Search for the next 512? bytes from noadfile in adfile
    search = noadfile[advance + noadadvance:advance + noadadvance + 512]

    print(search[0:16])
    adadvance = adfile.index(search)
    diffarr.append(adadvance)
    print("end ad {}: {}".format(sys.argv[2], adadvance))
    noadadvance += advance

    print("-"*20)

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
        file = open(folder+str(fileCount)+filenameString,"wb")
        fileCount = fileCount+1
        pos=startpos+i*segmentBitLength
        file.write(adfile[pos:pos+segmentBitLength])
        file.close()
    file = open(filenameString,"wb")