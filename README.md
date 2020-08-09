randopass
===

Generate memorable but cryptographically strong random word passphrases for your users. 

---
The problem with users selecting passphrases is that people have limited vocabularies and choose decidedly non-random words.

randopass uses the secrets library and a list of 3254 (at this time) words acquired from a hack to a web app using the Wordnik API. The default 4-word phrase then truly represents one of over 112 trillion combinations, or nearly 47 bits of randomness.

### Installation:
```bash
python -m pip install randopass
```

### As a library:

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
```python
$ python -m randopass
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

With parameter:
```python
$ python -m randopass 10
```
or
```bash
randopass 10
```

Example output:
```bash
Passphrase:
 crusadeelectviablesystembowelpushmarketingflatwareabsorbtrain
```
