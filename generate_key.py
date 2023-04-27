from Crypto.Cipher import AES

key = b"TheAkshathamkkey"
nonce = b"TheAkshathamkNce"

cipher = AES.new(key, AES.MODE_EAX, nonce)
ciphertext = cipher.encrypt(b"Hello World!")

print(ciphertext)

cipher = AES.new(key, AES.MODE_EAX, nonce)
print(cipher.decrypt(ciphertext))