def encode(message): 
	cipherText = ""
	for ch in message:
	    if ch.isalpha():
	      character = ord(ch) + 13
	      if character > ord('z'):
	        character -= 26
	      finalletter = chr(character)
	      cipherText += finalletter
	print ("Your ciphertext is: ", cipherText)
	return cipherText


def decode(cipherText):
	plainText = ""
	for ch in cipherText:
	    if ch.isalpha():
	      character = ord(ch) - 13
	      if character < ord('a'):
	        character += 26
	      finalletter = chr(character)
	      plainText += finalletter
	print ("Your plaintext is: ", plainText)
	return plainText

message=input("Enter any message you want to encode and decode: ")
encoded_message=encode(message);
decoded_message=decode(encoded_message)
