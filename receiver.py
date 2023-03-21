import socket 
import tqdm 

from Crypto.Cipher import AES

key = b"TheAkshathamkkey"
nonce = b"TheAkshathamkNce"

cipher = AES.new(key, AES.MODE_EAX, nonce)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost",9999))
server.listen()

client, adde = server.accept()


file_name = client.recv(1024).decode("utf-8")
print(file_name)
file_size = client.recv(1024).decode("utf-16-le")
print(file_size)


file= open(file_name, "wb")

done =False

file_bytes = b""



while not done:
    data =client.recv(1024)
    if file_bytes[-5:] == b"<END>":
        done = True
    else:
        file_bytes +=data
    

file.write(cipher.decrypt(file_bytes[:-5]))

file.close()
client.close()
server.close()
