from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from pbkdf2 import PBKDF2
import getpass,sys
import GetFiles

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
        return key
            
  def AESEncrypt(self,key,IV,source):
    files=GetFiles.getfiles(source)
    for a_file in files:
    	f=open(a_file,"r")
        fstream=f.read()
        f.close()
        source_ext=source[-3:]
        AES_stream=AES.new(key,AES.MODE_CFB,IV)
        AES_encrypted=AES_stream.encrypt(fstream)
        dest=str(a_file)[:-2]+'csy'
        with open(dest,"w") as write_file:
        	write_file.write(str(IV)+source_ext+AES_encrypted)
        
        
  def AESDecrypt(self,key,IV,source):
    f=open(source,"r")
    fstream=f.read()
    f.close()
    dest_ext=fstream[16:19]
    print dest_ext
    dest=source[:-3]+dest_ext
    AES_stream=AES.new(key,AES.MODE_CFB,IV)
    AES_decrypted=AES_stream.decrypt(fstream[19:])
    with open(dest,"w") as write_file:
        write_file.write(AES_decrypted)
