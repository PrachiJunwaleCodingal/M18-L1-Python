#Check the character

ch = input("Please Enter a Character : ")

if((ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')): 
    print( ch, "is an Alphabet") 
elif(ch >= '0' and ch <= '9'): 
    print(ch, "is a Digit")
else: 
    print(ch, "is a special Character")