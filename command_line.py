#!/usr/bin/env python3

import randopass
import sys

def main():
    numWords = 4
    args = [a for a in sys.argv[1:]]
    if(len(args)>0):
        numWords = args[0]
        try:
            numWords = int(args[0])
        except:
            print("invalid argument", file=sys.stderr)
            return
    phrase = ''.join(randopass.getPass(numWords))
    print('Passphrase:\n', phrase, file=sys.stdout)
    del phrase

if __name__ == "__main__":
    main()
