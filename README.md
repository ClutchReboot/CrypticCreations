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

x = CrypticCreations.CipherCreation(text='Sentence to be enciphered.')
x.caeser(shift=3)
print(f"Message: {x.initial_string}")
print(f"Enciphered Message: {x.creation}")
```

### Sample Output
```text
Message: Sentence to be enciphered.
Enciphered Message: Vhqwhqfh wr eh hqflskhuhg.
```