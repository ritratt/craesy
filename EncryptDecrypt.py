from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import getpass

class ED(object):
  def getfromuser(self,choice):
    if choice=='key':
        key=getpass.getpass('Enter AES Key (minimum 16 characters): ')
        if len(key)<16:
            print 'Key entered too short. Please try again.'
            self.getfromuser(choice)
        key=key+str(8-len(key)%8)*(8-len(key)%8)
        return key
    if choice=='IV':
        IV_seed=raw_input('Enter a seed for the IV: ')
        IV=SHA256.new()
        IV.update(IV_seed)
        IV.digest()
        return str(IV)[0:16]
        
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
