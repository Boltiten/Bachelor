import pathlib
import numpy as np
import sys
import csv
#TODO write code that does this automatically for all folders
#TODO unit tests
noAdLoc = sys.argv[1]
adLoc = sys.argv[2]
#Example command for running the program
# python audioDiffPointsSys.py "C:/Users/Thomas/Downloads/-tor-The EPA's Lies About Air Pollution Are Killing Americans.mp3" "C:/Users/Thomas/Downloads/-nor-The EPA's Lies About Air Pollution Are Killing Americans.mp3"
noAdFrames = np.fromfile(noAdLoc, dtype='uint8')
adFrames = np.fromfile(adLoc, dtype='uint8')

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
    pointArr = []
    pointArr.append(getFileName(sys.argv[1]))
    while i<len(noAdFrames):
        while((noAdFrames[i]==adFrames[y]) and i<len(noAdFrames) ):
            if(i+2>len(noAdFrames)):
                print("finished")
                break
            i=i+1
            y=y+1
        ret=findMatchWindow(10,noAdFrames,adFrames,i,y)
        if(not ret[1]):
            break
        pointArr.append(y)
        pointArr.append(ret[0])
        y=ret[0]
        print(i," ",y)
    print("exit")
    file = open('adBreakpoints.csv','a', newline="")
    writer = csv.writer(file)
    writer.writerow(pointArr)
    file.close()

def getFileName(filePath):
    path = pathlib.PurePath(filePath)
    return path.parent.parent.name+ "," + path.parent.name +","+ path.name


if __name__ == "__main__":
    main()
