import string
import binascii
from secret import MSG #Need to find what this does
#MSG is used as a paramater for encryption() on line 12

def encryption(msg):
    ct = [] #Makes an empty list 
    for char in msg:
	#Order of operations
        ct.append((123 * char + 18) % 256) #This part is the part that does it
    return bytes(ct)

ct = encryption(MSG)
f = open('./msg.enc','w')
f.write(ct.hex())
f.close()

def encrypt(x): #This will encrypt just like the og function
 return ((123 * x + 18) % 256 )
open("msg.enc") as y #Gets the message
ogmsg = binascii.unhexlify(y.read())

#idk 
