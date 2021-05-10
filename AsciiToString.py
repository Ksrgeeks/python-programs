def AsciiToString(num):
    ls=num.split(" ")
    
    for i in range(0,len(ls)) :
        print(chr(int(ls[i])),end="")

num='72 101 108 108 111 32 87 111 114 108 100 32 33'
AsciiToString(num)
