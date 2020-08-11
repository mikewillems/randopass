randopass
===

Generate memorable but cryptographically strong random word passphrases for your users. 

---
The problem with users selecting passphrases is that people have limited vocabularies and choose decidedly non-random words.

randopass uses the secrets library and a list of 58,110 (currently) English words from [http://www.mieliestronk.com/](mieliestronk.com). The default 4-word phrase from the full-length English dictionary then represents a random choice from over 100 billion trillion combinations, or nearly 77 bits of randomness.

Future development will enable use of a 3,254 common-word simple English dictionary from [https://www.wordnik.com/](Wordnik) and a list 51,478 words in Afrikaans - they're included in the source in case you want to switch manually.

Phrases can be generated with lower case, Capital case, or UPPER case capitalization, and defaults to all words of the passphrase being lower case. You can also used mixed case, where the case of any word is randomly selected, adding another 2^n bits of randomness where n is the number of words. Just for fun, I've also thrown in a WiLD case which randomly capitalizes each character. This adds roughly 2^(6n) bits of randomness where n is again the number of words in the passphrase.

Special characters are not supported, as they run contrary to the point of the library.

### Installation:
```bash
python -m pip install randopass
```

### As a library:
Remember that the python implementation returns a list of the component words.

```python
from randopass import getPass
passWords=getPass()
for word in passWords:
    print(word)
passPhrase = ''.join(passWords)
print('Your passphrase is ',passPhrase)
hash=someSaltingHashFunction(passPhrase)
del passPhrase
```

Example output:
```
poor
longitudinal
Yankee
garden
Your passphrase is poorlongitudinalYankeegarden
```

You can also specify a different number of words. 
```python
print(getPass(6))
```

Example output:
```
['option', 'ideology', 'variety', 'dedicate', 'warm', 'timetable']
```

### As a CLI tool for yourself:

Default usage:
```bash
python -m randopass
```

or
```bash
randopass
```

Example output:
```bash
Passphrase:
 brilliancelaboursweetstruggle
```

---
Usage with parameter:
```python
$ python -m randopass 10
```
or
```bash
$ randopass 10
```

Example output:
```bash
Passphrase:
 crusadeelectviablesystembowelpushmarketingflatwareabsorbtrain
```


```bash
$ python -m randopass upper 3
```

Example output:
```bash
Passphrase:
 WHIRRSUBHARMONICSGOURMETS
```

```bash
$ randopass 6 capital
```

Example output:
```
Passphrase:
 BibCompoundVirileBumpyOutcastsOutweighed
```