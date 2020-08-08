#!/usr/bin/env python3

import randopass
import sys

def main():
    numWords = -1
    args = [a for a in sys.argv[1:]]
    if(len(args)>0):
        numWords = args[0]
        try:
            numWords = int(args[0])
        except:
            print("invalid argument")
            return
        print('Passphrase:\n',''.join(randopass.getPass(numWords)))
    else:
        print('Passphrase:\n',''.join(randopass.getPass()))

if __name__ == "__main__":
    main()
