"""
randopass: strong random English-word passphrases
"""
__version__="0.1.3"

"""secrets package is used for randomness"""
import secrets
import sys
import importlib
from randopass.dictionaries import english
from randopass.dictionaries import english_simple
from randopass.dictionaries import afrikaans

capitalizations = ['lower', 'capital', 'upper', 'any', 'wild']
languages = ['english', 'english_simple', 'afrikaans']
dictionary = english.words()

def getVersion():
    return __version__

def main():
    numWords = 4
    capitalization = capitalizations[0]
    language = languages[0]
    args = [a for a in sys.argv[1:]]
    for arg in args:
        try:
            numWords = int(arg)
        except:
            if arg in capitalizations:
                capitalization = arg
            elif arg in languages:
                language = arg
            else: 
                print("invalid argument", file=sys.stderr)
                return
    language_module = importlib.import_module('randopass.dictionaries.'+language)
    dictionary = language_module.words()
    phrase = ''.join(getPass(numWords, capitalization, dictionary))
    print('Passphrase:\n', phrase, file=sys.stdout)
    del phrase

def getPass(length=4, capitalization=capitalizations[0], language=languages[0]):
    """returns passphrase composed of _length_ random words (4 by default)"""

    def capitalize(string, capitalization):
        capitalization = capitalization.lower()
        if capitalization == "upper":
            return string.upper()
        elif capitalization == "capital":
            return string.capitalize()
        elif capitalization == "any":
            return capitalize(string, secrets.choice(list(Capitalization)[:-2]))
        elif capitalization == "wild":
            return ''.join([capitalize(char, secrets.choice(list(Capitalization)[:-2])) for char in string])
        else:
            return string.lower()

    return [capitalize(secrets.choice(dictionary), capitalization) for i in range(length)]

