import json
from pprint import pprint
from ctypes.wintypes import tagSIZE

#start getStopWordList
def getStopWordList(stopWordListFileName):

    #read the stopwords file and build a list
    stopWords = []
    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords
#end

stopWordList=getStopWordList(r'D:\aldahw\stopwordsList.txt')
print stopWordList

data_json=open(r'D:\aldahw\res.json').read()
data=json.loads(data_json)

pprint(data)
#for x in range(len(data)):
print data[0]['caption']

def getHashTags(lines):
    #returns a list of words not present in the stopwords list

    hashTagList = []
    #split lines into words
    words = lines.split()
    for w in words:
        #ignore if it is a stop word
        if(w in stopWordList):
            continue
        else:
            hashTagList.append(w.lower())
    return hashTagList


#for x in range(len(data)):
alltags=getHashTags(data[0]['caption'])
print alltags


#resultFile=open('tags.txt','w')

#Removing duplicate tags
tags=[]
for x in alltags:
    if ('#'+str(x)) not in tags:
        temp=str(x)
        #resultFile.write('#')
        #resultFile.write(temp)
        #resultFile.write('\n')
        tags.append('#'+temp)
        
#resultFile.close()
print tags