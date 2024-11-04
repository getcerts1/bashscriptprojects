
#cipherstore = []


#inputvalue = int(input('how many numbers? '))



#for i in range(inputvalue):
  #inputletter = input('choose a letter ')
  #cipherstore.append(chr((ord(inputletter) - ord('a') + inputvalue) % 26 + ord('a')))



#ciphertext = ''.join(cipherstore)
#print(ciphertext)





import string
import time
inputshift = int(input('Enter a shift value: \n'))
inputlist = input('Type text: \n')

def cipherbuilder(inputshift, inputlist):
    
    cipherstore = []
    
    for letter in inputlist:
        # Check if the letter is lowercase
        if 'a' <= letter <= 'z':
            new_letter = chr((ord(letter) - ord('a') + inputshift) % 26 + ord('a'))
        # Check if the letter is uppercase
        elif 'A' <= letter <= 'Z':
            new_letter = chr((ord(letter) - ord('A') + inputshift) % 26 + ord('A'))
        else:
            new_letter = letter  ### Keep the character unchanged if it's not a letter
            
        cipherstore.append(new_letter)
    

    ciphertext = ''.join(cipherstore)
    return ciphertext

output = cipherbuilder(inputshift)
print(output)
