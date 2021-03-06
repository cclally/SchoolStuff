#Chase Lally
#02/11/16
#Vignere Cipher Example in Python 3.4       #This is more of a ECB(Electronic Code Block) Encryption Example. These encryptions are incredibly out-datted
#Incredibly ineffecient script with multiple string , and int declares that definitely could have been shortened
#     but you should get the idea on how this works.

originKey = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ,.-_") # Origin Key from Modulus base 30
text = input('Enter Plain Text: ')
plainText = list(text.upper())  # Uppercase the plainText to compare with the originKey
lowkey = input('Enter Key for Cipher: ')

key = list(lowkey.upper())     # same as plainText obviously
cipherText = list() #initialize a empty list to add elements to.
k = len(lowkey) #k will be the key length and will define where the block of the cipher will continue if the plainText is longer than the key
i = 0
j = 0
pTi = 0
ki = 0
cKNum = 0
m = 0

for index in range(len(plainText)):  #scales the entire list
    a = plainText[index]  # Gets the character in the list at that given point in the index
    pTi = originKey.index(a) # gets the previous characters key value based on its index in originKey and stores the value for computation
    b = key[i] 
    #key.remove(b) # just removes the point 0 from the array at that point and repopulates the list from its following element until empty.
    ki = originKey.index(b)
    cKNum = (pTi + ki)%30 # adds the two values into cKNum to determine the CipherCharacter.
    #if (cKNum > 29): #breaks in here if it goes out of bounds of the originKey and then decrements 30 to start over along the array of elements.
       # cKNum -= 30
    c = originKey[cKNum]
    cipherText.insert(index, c) #slowly adding the new cipherCharacter in to the character array at that current index.
    print("This is the length of Cipher text")
    print(len(cipherText))
    k -= 1 # break into the if once the key goes through 10 iterations, and then re-supply part of the cipherText as a new block of the key.
    i += 1
    m += 1
    if (k == 0):
        while ((j < len(cipherText)) ):
            d = cipherText[j]
            key.insert(i, d)
            j += 1
            i += 1
            k += 1
        i -= 3
        

cipherText = ''.join(cipherText) #form the character array into a string type.
print(cipherText)



## THIS IS THE DECRYPTION OF OUR MESSAGES

plainText = list()
i = 0
j = 0
pTi = 0
ki = 0
cKNum = 0

for index in range(len(cipherText)):  #scales the entire list
    a = cipherText[index]  # Gets the character in the list at that given point in the index
    pTi = originKey.index(a) # gets the previous characters key value based on its index in originKey and stores the value for computation
    b = key[i] 
    #key.remove(b) # just removes the point 0 from the array at that point and repopulates the list from its following element until empty.
    ki = originKey.index(b)
    cKNum = (pTi - ki)%30 # subtracts the two values into cKNum to determine the MessageCharacter.
    #if (cKNum > 29): #breaks in here if it goes out of bounds of the originKey and then decrements 30 to start over along the array of elements.
       # cKNum -= 30
    c = originKey[cKNum]
    plainText.insert(index, c) #slowly decrypting the MessageCharacters in to the character array at that current index.
    print("This is the length of Cipher text")
    print(len(plainText))
    i += 1
   

plainText = ''.join(plainText) #form the character array into a string type.
print(plainText)
