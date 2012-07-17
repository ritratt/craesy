from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from pbkdf2 import PBKDF2
import getpass,sys

class ED(object):
  def getfromuser(self,*args):
    try:
        choice=args[0]
        IV=args[1]
    except IndexError:
        print 'Error processing IV.'
        sys.exit()
        
    if choice=='key':
        password=getpass.getpass('Enter AES your password: \n>')
        key=PBKDF2(password,IV).read(32)
        print key
        return key
            
  def AESEncrypt(self,key,IV,source,dest):
    print source,dest
    f=open(source,"r")
    fstream=f.read()
    f.close()
    print 'slut'
    AES_stream=AES.new(key,AES.MODE_CFB,IV)
    AES_encrypted=AES_stream.encrypt(fstream)
    print 'crapola'
    with open(dest,"w") as write_file:
        write_file.write(str(IV)+AES_encrypted)
        
        
  def AESDecrypt(self,key,IV,source,dest):
    f=open(source,"r")
    fstream=f.read()[16:]
    f.close()
    AES_stream=AES.new(key,AES.MODE_CFB,IV)
    AES_decrypted=AES_stream.decrypt(fstream)
    with open(dest,"w") as write_file:
        write_file.write(AES_decrypted)
