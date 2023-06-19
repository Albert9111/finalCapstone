
text = input("Enter your text: \t")
n = 15                                                          # it will give the 15th letter after the input letter

def encrypt(text,n):
    code = " "
    
    for i in range(len(text)):                                  # iterate over the text
        letter = text[i]

        if (letter.isupper()):                                  # check if a character is uppercase
            code += chr((ord(letter) + n - 65) % 26 + 65)
        
        elif (letter.islower()):                                # check if a character is lowercase 
            code += chr((ord(letter) + n - 97) % 26 + 97)
        
        elif letter == " ":                                     # check if there is space  
            code += " "
        
        else:                                                   # ask the user to enter a valid input
            letter != str
            print("Please enter a text!")
            
    return code




print("Cipher: " + encrypt(text,n))