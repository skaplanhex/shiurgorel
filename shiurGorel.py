#! /usr/bin/env python

import numpy.random as rand
import sys

#acceptable options
options = ("shiur","beer","food")
optionDict = {"shiur":0,"beer":1,"food":2}
nameDict = {0:"Shalom",1:"Jordan",2:"Moshe",3:"Andrew",4:"Avi",5:"Yoni",6:"Elad",7:"Eli",8:"Meir",9:"Yehoshua",10:"Eitan",11:"Dov"}

def printUsage():
    print ""
    print "Usage: ./shiurGorel.py <what-to-generate>"
    print ""
    print "Options for <what-to-generate>: shiur, beer, food"
    print "If no options given, all are generated"
    print ""
    sys.exit(1)

#function to return shiur history for last 5 weeks instead of last 2 weeks for beer/food
def getShiurHistory():
    f = open("history.txt",'r') #open just to read
    lines = f.readlines()
    if ( len(lines) < 6): #if there aren't at least five weeks of history and the header
        print "Something's messed up with the history...check it out!"
        sys.exit(1)
    names=[]
    for i in range(1,6): #get last 5 maggidei shiur
        names.append( lines[-i].split()[0] )
    f.close()
    return names



#return tuple of lists with last two weeks of shiur, beer, and food history
#assumes that the last two lines are valid history lines (they should be)
def getHistory():
    f = open("history.txt",'r') #open just to read
    lines = f.readlines()
    if ( len(lines) < 3): #if there aren't at least two weeks of history and the header
        print "Something's messed up with the history...check it out!"
        sys.exit(1)
    twoWeeksAgo = lines[-2].split()
    oneWeekAgo = lines[-1].split()
    if len(twoWeeksAgo) != 3 or len(oneWeekAgo) != 3:
        print "Something's messed up with the end of the history...check it out!"
        sys.exit(1)
    shiurHistory = getShiurHistory()
    beerHistory = [oneWeekAgo[1],twoWeeksAgo[1]]
    foodHistory = [oneWeekAgo[2],twoWeeksAgo[2]]
    f.close()
    return (shiurHistory,beerHistory,foodHistory)

def get(num):
    if num > 2:
        print "you fail"
        sys.exit(1)
    else:
        fullHistory = getHistory()
        history = fullHistory[num]
        if num == 1:
            history += fullHistory[2]
        elif num == 2:
            history += fullHistory[1]
        nameToReturn = ""
        done = False
        while not done:
            draw = rand.randint( 0,len(nameDict) )
            nameDrawn = nameDict[draw]
            if nameDrawn not in history:
                nameToReturn = nameDrawn
                done = True
        return nameToReturn

def getShiur():
    return get(0)
def getBeer():
    return get(1)
def getFood():
    return get(2)

#reimplemented to save a few microseconds by not opening the same file 3 times
def getAll():
    history = getHistory()
    shiurHistory = history[0]
    beerHistory = history[1]
    foodHistory = history[2] + beerHistory #to make it impossible for someone to bring something every week

    #do shiur, beer, and food seperately
    shiur = ""
    beer = ""
    food = ""

    shiurDone = False
    beerDone = False
    foodDone = False

    while not shiurDone:
        num = rand.randint( 0,len(nameDict) )
        nameDrawn = nameDict[num]
        if nameDrawn not in shiurHistory:
            shiur = nameDrawn
            shiurDone = True

    while not beerDone:
        num = rand.randint( 0,len(nameDict) )
        nameDrawn = nameDict[num]
        if nameDrawn not in foodHistory and nameDrawn != shiur:
            beer = nameDrawn
            beerDone = True

    while not foodDone:
        num = rand.randint( 0,len(nameDict) )
        nameDrawn = nameDict[num]
        if nameDrawn not in foodHistory and nameDrawn != beer and nameDrawn != shiur:
            food = nameDrawn
            foodDone = True
    return (shiur,beer,food)

def main():
    #make sure input is right
    if ( len(sys.argv) > 2 ):
        printUsage()

    elif ( len(sys.argv) == 2 ):
        option = sys.argv[1].lower() #convert to lowercase to not be annoying
        if not option in options:
            printUsage()
        name = get( optionDict[option] )
        print "%s: "%option + name
        
    #if no options given, do them all
    else:
        names = getAll()
        f = file("history.txt","a")
        lineToAdd = names[0] + " " + names[1] + " " + names[2] + "\n"
        f.write(lineToAdd)
        f.close()
        print "Shiur: " + names[0]
        print "Beer: " + names[1]
        print "Food: " + names[2]

if __name__ == "__main__":
    main()