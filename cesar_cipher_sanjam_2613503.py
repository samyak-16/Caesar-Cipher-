import string 
import os 


# This module prints the information  about the program and welcomes the user using the program .
def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")
    

# welcome()

# This module or function helps user to take input for modeOfConversion , message , shiftnumber  and validate it through infinite loops once fully validated it breaks the loop and proceeds to next step or logic .
def enter_message():
    
    while  True : 
        modeOfConversion =  input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if(modeOfConversion  in["e","d"]):
            break
        else:
            print("Invalid Mode")

    if(modeOfConversion == "e"):
        message = input("What message would you like to encrypt: ").upper()
    else:
        message = input("What message would you like to decrypt: ").upper()
    
    while True :
        try : 
            shiftNumber =  int(input("What is the shift number: "))
            break
        except ValueError :
            print("Invalid Shift")
    return (
        modeOfConversion,message,shiftNumber
    )

# print(enter_message()) 
# print(string.ascii_uppercase)
capitalLetters = string.ascii_uppercase #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphaList = list(capitalLetters) #["A","B","C","D",...,"Z"]


# It encrypts the message with the given shift number using some mathmatical logic 
def encrypt(message,shift):
    #message is expected to be in upper case - handled by enter message fn 
    encryptedmessage  = ""
    for i in message.upper( ) :
        if(i not in alphaList):
            encryptedmessage+=i
        else:
            originalLetterIndex = alphaList.index(i)
            encryptedLetterIndex = originalLetterIndex+shift
            encryptedLetter = alphaList[encryptedLetterIndex % len(alphaList)]
            encryptedmessage+=encryptedLetter
    
    return encryptedmessage

# print(encrypt("I LOVE YOU",4))

# It decrypt messages based on the shift number using mathmatical logic .
def decrypt(message,shift):
    
    #message is expected to be in upper case - handled by enter message fn 
    decryptedmessage  = ""
    for i in message.upper() :
        if(i not in alphaList):
            decryptedmessage+=i
        else:
            encryptedLetterIndex = alphaList.index(i)
            originalLetterIndex =  encryptedLetterIndex-shift
            originalLetter = alphaList[originalLetterIndex % len(alphaList)]
            decryptedmessage+=originalLetter
    
    return decryptedmessage


# print(decrypt("LIPPS ASVPH",4))

#---------------------------------------------------------------------------------------------------------------------------------------

# File Input/Output (25%):

# This module / function  takes fileName , mode , shiftNumber as function paramater , it processes the file and returns the list of  (encrypted/decrypted messsages) by processsing the file content  as per the given mode in the fn paramater. 
def process_file(fileName, mode,shiftNumber):
    #, returning a list of encrypted/decrypted messages.

    with open(fileName) as f : 
        messages =[]
        if(mode=="e"):
            for line in f:
                messages.append(encrypt(line.strip().upper(),shiftNumber)+"\n") # shift is missing , will implement later 
        else:
            for line in f :
                messages.append(decrypt(line.strip().upper(),shiftNumber)+"\n") # shift is missing, will implement later
    return messages


# This functions takes the fileName as the input and returns if the file is present inside the same directory/folder  or not . 
def is_file(fileName):
    return os.path.exists(fileName)

# print(is_file("message.txt"))


# It takes the list of encrypted/decrypted messages and writes them into results.txt 
def write_messages(messages=[]): # messages is a list of multiple strings / message
    with open("results.txt","w") as f:
        f.writelines(messages)
    

# This is one of the module where most of the logic is written , logic includes , asking user for selecting mode in which the want to encrypt / decrypt using ( file or console ) and other logic are same as previous enter_message() module - Code is somehow repeated :)
def message_or_file():
    while  True : 
        modeOfConversion =  input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if(modeOfConversion in["e","d"]):
            break
        else:
            print("Invalid Mode")

    # if(modeOfConversion == "e"):
    #     message = input("What message would you like to encrypt: ").upper()
    # else:
    #     message = input("What message would you like to decrypt: ").upper()
    
    # while True :
    #     try : 
    #         shiftNumber =  int(input("What is the shift number: "))
    #         break
    #     except ValueError :
    #         print("Invalid Shift")
    while True : 
        userOption = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if(userOption in ["f","c"]):
            break
        else :
            print("Invalid Option")
    
    if(userOption=="f"):
        while True :
            fileName = input("Enter a filename: ")
            if(is_file(fileName)):
                break
            else:
                    print("Invalid Filename")
        if(modeOfConversion=="e"):
            while True :
             try : 
                shiftNumber =  int(input("What is the shift number: "))
                break
             except ValueError :
                 print("Invalid Shift")
            encryptedMessages = process_file(fileName,"e",shiftNumber)
            write_messages(encryptedMessages)
            print("Output written to results.txt")
            # return (modeOfConversion,)
            
        else : #d
            while True :
             try : 
                shiftNumber =  int(input("What is the shift number: "))
                break
             except ValueError :
                 print("Invalid Shift")
            decryptedMessages = process_file(fileName,"d",shiftNumber)
            write_messages(decryptedMessages)
            print("Output written to results.txt")
            
            
        
    else:
        if(modeOfConversion=="e"):
            message = input("What message would you like to encrypt: ").upper()
            while True :
             try : 
                shiftNumber =  int(input("What is the shift number: "))
                break
             except ValueError :
                 print("Invalid Shift")
            encryptedMessage = encrypt(message,shiftNumber)
            print(encryptedMessage)
        else:
            message = input("What message would you like to decrypt: ").upper( )
            while True :
             try : 
                shiftNumber =  int(input("What is the shift number: "))
                break
             except ValueError :
                 print("Invalid Shift")
            decryptedMessage = decrypt(message,shiftNumber)
            print(decryptedMessage)
    if(userOption=="f"):
        return (modeOfConversion,None ,fileName)  
    else:
        return (modeOfConversion,message,None)      
            

# This is the main function which runs in the runtime and joins other modules together ;
def main():
    welcome()
    while True :
        message_or_file()
        while True:
            userInput = input("Would you like to encrypt or decrypt another message? (y/n): ")
            if(userInput  in ["y","n"]):
                break
            else:
                print("Invalid Option Choosed")
        if(userInput=="n"):
            print("Thanks for using the program, goodbye! ")
            break
        
           
           
            


# mode , message/None , filename/None 

main()