# CrypticCreations
Create ciphers or random strings for DnD players to try and read aloud for the group.

## RandomCreation
### Usage
```python
import CrypticCreations

x = CrypticCreations.RandomCreation()
x.paragraph()
x.sprinkle_words(additional_words=['WORDs', 'THAT', "WONT", "CHANGE"])
print(f'{x.creation}')
```
### Sample Output
```text
Lzquwzyuwi zot rqieeuue etouzyij WORDs erpaxupeh. Nwpeb axfixse THAT Clgu zheihyaa mrdak jleasleu WONT gueoqovexa. Bcsuiraz iwfuzytek CHANGE emeoxawkja.
```

## CipherCreation
### Usage
```python
import CrypticCreations

x = CrypticCreations.CipherCreation(text='Sentence to be ciphered.')
x.caeser(shift=3)
print(f"Message: {x.text}")
print(f"Enciphered Message: {x.creation}")
```

### Sample Output
```text
Message: Sentence to be ciphered.
Enciphered Message: Vhqwhqfh wr eh flskhuhg.
```