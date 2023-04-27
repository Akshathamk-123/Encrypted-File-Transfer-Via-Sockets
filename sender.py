import os 
import socket

from Crypto.Cipher import AES
#The Advanced Encryption Standard (AES) is a symmetric block cipher algorithm that is widely used for secure data encryption and decryption.
key = b"TheAkshathamkkey"
#Key is essentially a sequence of random bits that determines how the encryption algorithm transforms the plaintext into ciphertext and vice versa. 
nonce = b"TheAkshathamkNce"
#Stands for number used once 
#It is a random number that is used only once in a cryptographic communication to prevent replay attacks.


cipher = AES.new(key, AES.MODE_EAX, nonce)
#initializes a new instance of the Advanced Encryption Standard (AES) cipher in the EAX mode of operation, using the given key and nonce values.

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#The AF_INET is the internet address family for the IPv4
#SOCK_STREAM is for the soket type for TCP
client.connect(("192.168.191.221" , 9999))
#To file transfer between two machines: The localhost has to be replaced with the IP Address of the Server or replace it with any

file_size = os.path.getsize("file")
#Gets the size of the file

#Opening with the read mode
with open("file", "rb") as f:
    data = f.read()

#Encrypting the data
encrypted = cipher.encrypt(data)

#Sending the name of the file.txt after encoding
client.send("file.txt".encode(encoding='utf-8'))
#Sending the file size after encoding
client.send(str(file_size).encode(encoding='utf-16-le'))
#Sending the whole file that is encrypted
client.sendall(encrypted)
#Last five characters are the <END> so that it gets easy to stop the loop
client.send(b"<END>")

client.close()