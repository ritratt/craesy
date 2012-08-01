from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from pbkdf2 import PBKDF2
import getpass,sys,random
import GetFiles

class ED(object):
  	def generatekey(self,password,IV):
   # try:
    #    choice=args[0]
     #   IV=args[1]
   # except IndexError:
    #    print 'Error processing IV.'
     #   sys.exit()
        
   # if choice=='key':
		key=PBKDF2(password,IV).read(32)
        	return key
	def getfromuser(self,choice):
		if choice=='password':
	        	password=getpass.getpass('Enter AES your password: \n>')
			return password
	def AESEncrypt(self,password,source):
		files=GetFiles.getfiles(source)
		for a_file in files:
    			f=open(a_file,"r")
        		fstream=f.read()
        		f.close()
			IV=SHA256.new(str(random.randint(0,2**100))).hexdigest()[0:16]
			key=self.generatekey(password,IV)
        		source_ext=a_file[-3:]
        		AES_stream=AES.new(key,AES.MODE_CFB,IV)
        		AES_encrypted=AES_stream.encrypt(fstream)
        		dest=str(a_file)[:-3]+'csy'
        		with open(dest,"w") as write_file:
				write_file.write(str(IV)+source_ext+AES_encrypted)
		print 'Encryption done!'
        
        
	def AESDecrypt(self,password,source):
		files=GetFiles.getfiles(source)
    		for a_file in files:
			f=open(a_file,"r")
			fstream=f.read()
			f.close()
			IV=fstream[0:16]
			key=self.generatekey(password,IV)
			dest_ext=fstream[16:19]
			dest=a_file[:-3]+dest_ext
			AES_stream=AES.new(key,AES.MODE_CFB,IV)
			AES_decrypted=AES_stream.decrypt(fstream[19:])
			with open(dest,"w") as write_file:
				write_file.write(AES_decrypted)
		print 'Decryption done!'
