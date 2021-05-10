def missingNumber(lst) :
    sum = 0
    for i in range(0,len(lst)) :
        sum = sum + lst[i]
        i=+1
        
    n = lst[-1]
    missNum = n*(n+1)/2 - sum
    print("Missing Number is : ",missNum)

a = [1,2,3,4,5,6,7,8,10,11]
missingNumber(a)
