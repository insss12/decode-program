import random
import string

chars= " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key=chars.copy()

random.shuffle(key)
while True:
    print("---------------------------------------------")
    option=input("choose what you want to do: ecrypt or decrypt ").lower()
    print("---------------------------------------------")
    if option == "ecrypt":
        
        text1= input("enter a message ")
        text2= " "
        print("---------------------------------------------")
        
        for letter in text1:
            index=chars.index(letter)
            text2=text2+key[index]
        
        
        print(f"you message:{text1}")
        print(f"translation:{text2}")
    elif option == "decrypt":
        text3=input("enter a code to decode ")
        text4=" "
        
        for zalo in text3:
            index=key.index(zalo)
            text4+=chars[index]
        print(f"you message:{text3}")
        print(f"translation:{text4}")