# Python program to print fibonacci series
def fibonacci(x,y,a):
    print(x,end=" ")
    print(y,end=" ")
    for i in range(0,a) :
        z=x+y
        print(z,end=" ")
        temp=y
        x=temp
        y=z
a=int(input("Enter the number of elements , you want to print of fibonacci series ."))
fibonacci(0,1,a)
