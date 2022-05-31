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

x = CrypticCreations.CipherCreation(text='Sentence that will be encoded.')
x.basic(shift=3)
print(f"Message: {x.initial_string}")
print(f"Encoded Message: {x.creation}")
```

### Sample Output
```text
Message: Sentence that will be encoded.
Encoded Message: Vhqwhqfh wkdw zloo eh hqfrghg.
```