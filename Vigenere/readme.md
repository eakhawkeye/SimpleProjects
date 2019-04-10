# Vigenère
A little python script to encrypt and decrypt messages using the Vigenère cipher.

###### Output: Basic Encryption
```
-$ vigenere.py -k secret -m 'special message'
     input: SPECIALMESSAGE
       key: SECRET
    output: KTGTMTDQGJWTYI
```

###### Output: Basic Decryption
```
-$ vigenere.py -k secret -m KTGTMTDQGJWTYI -d
     input: KTGTMTDQGJWTYI
       key: SECRET
    output: SPECIALMESSAGE
```

###### Output: Iterated Encryption (x10)
```
-$ vigenere.py -k secret -m 'special message' -i 10
     input: SPECIALMESSAGE
       key: SECRET
    output: KTGTMTDQGJWTYI
```

###### Output: Iterated Decryption (x10)
```
-$ vigenere.py -k secret -m KTGTMTDQGJWTYI -i 10 -d
     input: KTGTMTDQGJWTYI
       key: SECRET
    output: SPECIALMESSAG
```

###### Output: Encryption with NoNoneSense
```
-$ vigenere.py -k secret -m 'special message' -n
KTGTMTDQGJWTYI
```

## Usage
```
usage: vigenere.py [-h] --key KEY --message MESSAGE [--decrypt]
                   [--iterations ITERATIONS] [--nononsense]
```

