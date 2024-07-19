import random
chars ="qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLHGFDSAZXCVBNM1234567890!@#$%^&*()"
length=int(input("characterlength"))
password=""

for a in range(length):
  password+=random.choice(chars)
print(password)