
# coding: utf-8

# In[ ]:

s =raw_input("Frase a encriptar:")
key=int(input("Key:"))

encriptado=""
for i in s:
  if i.isalpha():
    if i.islower():
      encriptado= encriptado+chr(((ord(i)-97+key)%26)+97)
    else:
      encriptado= encriptado+chr(((ord(i)-65+key)%26)+65)
  else:
    encriptado= encriptado + i
print encriptado

