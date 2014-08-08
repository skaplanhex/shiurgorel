#! /usr/bin/env python

import numpy.random as rand
import sys

#acceptable options
options = ("shiur","beer","food")

def printUsage():
    print ""
    print "Usage: shiurGorel <what-to-generate>"
    print ""
    print "Options for <what-to-generate>: shiur, beer, food"
    print "If no options given, all are generated"
    print ""


def main():
    #make sure input is right
    if ( len(sys.argv) > 2 ):
        printUsage()
        sys.exit(1)
    elif ( len(sys.argv) == 2 ):
        option = sys.argv[1]
        if not option in options:
            printUsage()
            sys.exit(1)


if __name__ == "__main__":
    main()