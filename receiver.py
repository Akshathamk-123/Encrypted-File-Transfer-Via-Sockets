import socket 


from Crypto.Cipher import AES
#AES is Advancced Encryption Standard
#The Advanced Encryption Standard (AES) is a symmetric block cipher algorithm that is widely used for secure data encryption and decryption.
key = b"TheAkshathamkkey"
#Key is essentially a sequence of random bits that determines how the encryption algorithm transforms the plaintext into ciphertext and vice versa. 
nonce = b"TheAkshathamkNce"
#Stands for number used once 
#It is a random number that is used only once in a cryptographic communication to prevent replay attacks.

cipher = AES.new(key, AES.MODE_EAX, nonce)
#initializes a new instance of the Advanced Encryption Standard (AES) cipher in the EAX mode of operation, using the given key and nonce values.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#The AF_INET is the internet address family for the IPv4
#SOCK_STREAM is for the soket type for TCP
server.bind(("localhost",9999))
#To file transfer between two machines: The localhost has to be replaced with the IP Address of the Server
server.listen()

client, adde = server.accept()


file_name = client.recv(1024).decode("utf-8")
#receives data on a socket with descriptor socket and stores it in a buffer
print(file_name)
file_size = client.recv(1024).decode("utf-16-le")
print(file_size)


file= open(file_name, "wb")
#write mode


#Initialization
done =False

file_bytes = b""


#Reading the encrypted data except the last 5 characters because the last five characters are <END>
while not done:
    data =client.recv(1024)
    if file_bytes[-5:] == b"<END>":
        done = True
    else:
        file_bytes +=data
    
#Decrypting the whole file stored in the variable file_bytes
file.write(cipher.decrypt(file_bytes[:-5]))

file.close()
client.close()
server.close()
