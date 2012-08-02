craesy is a simple command line file encryption tool implemented in python for Linux OS. It uses AES to encrypt and decrypt the files.

Installation:
1. Download as zip and extract.
2. Run make as su.

Encryption:
craesy -e /path/to/folder.orfile 


Decryption:
craesy -d path/to/encrypted/folder.orfile 


The encrypted files are created in the same path as the source file with the same file name and extension as .csy.
e.g. craesy -e /home/foo.txt will create the encrypted file /home/foo.csy
