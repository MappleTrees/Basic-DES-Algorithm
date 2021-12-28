# import library
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

data = "Data ini akan dienkripsi"

# 8 byte block 
key = b'inikunci' 

# Menetapkan panjang data yang akan dienkripsi
BLOCK_SIZE = 32 

# encryption
des = DES.new(key, DES.MODE_ECB)
padded_text = pad(data.encode(), BLOCK_SIZE)
encrypted_text = des.encrypt(padded_text)

print(encrypted_text)

# decryption
key = b'inikunci' # 8 byte block
des = DES.new(key, DES.MODE_ECB)
decrypted_text = des.decrypt(encrypted_text)

print(decrypted_text.decode())