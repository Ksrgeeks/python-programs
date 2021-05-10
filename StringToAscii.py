# String to ASCII sequence

def StringToAscii(str):
    for i in str :
        print(ord(i),end=" ")
        # print(ord(i),end="")
        # To print Without spaces we use end=""

str=input("Enter a String ")
StringToAscii(str)


