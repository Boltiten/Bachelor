import pathlib
import numpy as np
import sys
import csv
#TODO unit tests
noAdLoc = sys.argv[1]
adLoc = sys.argv[2]
#Example command for running the program
# python AudioDiff.py "-tor-The EPA's Lies About Air Pollution Are Killing Americans.mp3" "-nor-The EPA's Lies About Air Pollution Are Killing Americans.mp3" 5000
# Note that the last sysarg is for bytelenght of segemntations, and you need ad + noad folder ready before running
noAdFrames = np.fromfile(noAdLoc, dtype='uint8')
adFrames = np.fromfile(adLoc, dtype='uint8')
fileCount = 0

#Finds an equal bytesequence for the two audio files
def findMatchWindow(windowsize, shorterArr, longerArr, shortPos, longPos):
    print(shortPos,"in loop")
    print(shortPos/len(noAdFrames))
    match = shorterArr[shortPos:(shortPos+windowsize)]
    foundMatch=True
    while(not (np.array_equal(longerArr[longPos:(windowsize+longPos)],match))):
        longPos=longPos+1
        if (longPos>len(longerArr)-windowsize):
            foundMatch=False
            break
    return(longPos,foundMatch)

def main():
    i=0
    y=0
    breakPointArr = []
    breakPointArr.append(getFileName(sys.argv[2],"/"))
    print(breakPointArr[0])
    finished = False
    while i<len(noAdFrames) or not finished:
        while((noAdFrames[i]==adFrames[y]) and i<len(noAdFrames) ):
            if(i+2>len(noAdFrames)):
                print("finished")
                finished = True
                break
            i=i+1
            y=y+1
        ret=findMatchWindow(100,noAdFrames,adFrames,i,y)
        if(not ret[1]):
            break
        breakPointArr.append(y)
        breakPointArr.append(ret[0])
        y=ret[0]
        print(i," ",y)
    csvFile = open('adBreakpoints.csv','a', newline="")
    fileString = getFileName(adLoc,",")
    csvWriter = csv.writer(csvFile, delimiter="|")
    csvWriter.writerow(breakPointArr)
    csvFile.close()
    prevSegLen = 0
    for i in range(1,(int)(len(breakPointArr))-1):
        prevSegLen = splitAudio(int(sys.argv[3]),breakPointArr[i],breakPointArr[i+1],fileString,i,prevSegLen)
    print("done")

def splitAudio(segmentBitLength,startpos,endpos,filenameString,oddMeansAd,prevNumOfFSegemntation):
    global fileCount
    fileBefore = fileCount
    if (oddMeansAd%2==1):
        ranVar = range((int)((endpos-startpos)/segmentBitLength))
        folder = "ad/"
    else:
        ranVar = range(prevNumOfFSegemntation*2)
        folder = "noad/"
    print(ranVar)
    for i in ranVar:
        file = open(folder+str(fileCount)+filenameString,"wb")
        fileCount = fileCount+1
        pos=startpos+i*segmentBitLength
        file.write(adFrames[pos:pos+segmentBitLength])
        file.close()
    file = open(filenameString,"wb")
    return(fileCount-fileBefore)

#For generating unique name for podcasts
def getFileName(filePath,delimeter):
    path = pathlib.PurePath(filePath)
    return path.parent.name +delimeter+ path.name

if __name__ == "__main__":
    main()
