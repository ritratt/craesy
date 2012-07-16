#!/usr/bin/python

from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import getpass,argparse,EncryptDecrypt,random
from sys import argv


    
try:
  script,mode,source_file,dest_file=argv
  if(mode=='-e'):
      edobj=EncryptDecrypt.ED()
      key=edobj.getfromuser('key')
      IV=SHA256.new(str(random.randint(0,2**100))).hexdigest()[0:16]
      print IV
      edobj.AESEncrypt(key,IV,source_file,dest_file)      
  elif(mode=='-d'):
      edobj=EncryptDecrypt.ED()
      key=edobj.getfromuser('key')
      with open(source_file,"r") as f_IV:
          IV=f_IV.read()[0:16]
      edobj.AESDecrypt(key,IV,source_file,dest_file)
except ValueError:
  if len(argv)>4:
    print 'Too many parameters passed. Please try again with 3 parameters.'
  elif len(argv)<4:
    print 'Too few parameters passed. Please try again with 3 parameters.'