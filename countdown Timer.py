import time

def countdown(t) :
    while t > 0 :
        print(t)
        t-=1
        time.sleep(1)
        
    print(" TIME OVER ")

print("Enter the time in Seconds for Countdown")
a = input()

while not a.isdigit() :
    print()
    a = input()
a = int(a)
countdown(a)
