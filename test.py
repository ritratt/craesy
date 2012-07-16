from Crypto.Hash import SHA256
from Crypto.Cipher import AES

def AESEncrypt(key,IV,source,dest):
    print source,dest
    f=open(source,"rb")
    fstream=f.read()
    f.close()
    print 'slut'
    AES_stream=AES.new(key,AES.MODE_CFB,IV)
    AES_encrypted=AES_stream.encrypt(fstream)
    #print AES_encrypted
    print 'crapola'
    with open(dest,"wb") as write_file:
        write_file.write(AES_encrypted)
        
        
def AESDecrypt(key,IV,source,dest):
    f=open(source,"rb")
    fstream=f.read()
    f.close()
    AES_stream=AES.new(key,AES.MODE_CFB,IV)
    AES_decrypted=AES_stream.decrypt(fstream)
    with open(dest,"wb") as write_file:
        write_file.write(AES_decrypted)
        
        
hash=SHA256.new('xx').digest()
#hash=str(hash)
print len(hash)

AESEncrypt(str(SHA256.new('abc').hexdigest())[0:16],str(hash)[0:16],'/home/ritratt/Documents/Code/eggy/x.jpg','/home/ritratt/Documents/y.aes')