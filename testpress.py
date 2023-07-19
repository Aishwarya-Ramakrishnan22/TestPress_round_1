#1. Reverse String

user_input = input("enter your String")
if(1<=len(user_input)<=100):
    if(user_input==user_input.lower()):
        for i in range(len(user_input)-1,-1,-1):
            print(user_input[i])   
    else:
        print("String must be in Lowercase... ")
else:
    print("String should have a length of 1-100...")
    
    
# 2. prime number or not

user_num= int(input("enter the number"))
num = False
def prime(num):
    if (user_num==1):
        print("it is not a prime number")
    elif(user_num>1):
        for i in range(2, user_num):
            if(user_num%i==0):
                num = True
                break
    if(num==True):
        print(user_num,"its not a prime")
    else:
        print(user_num,"its a prime")
prime(num)


#  3. Given an array of numbers, arrange them in a way that it forms the largest value.

from itertools import permutations
arr = [54, 546, 548, 60]
perms = permutations(arr)
largest = max(int(''.join(map(str, perm))) for perm in perms)
print(largest)


# 4. Given a number N, print reverse of number N.

num = int(input("enter the num"))
num = str(num)
op = ""
if(1<=int(num)<=10000):
    for i in range(len(num)-1,-1,-1):
        op+=num[i]
    print(op.lstrip('0'))    
    op = int(op)

else:
    print("Number should have 1 - 10000")


# 5. Given an array of numbers, find the maximum and minimum element in the array.

arr = [54, 546, 548, 60]
def numbers():
    max_num = arr[0]
    min_num = arr[0]
    for i in arr:
        if(max_num<i):
            max_num=i
        
        if(min_num>i):
            min_num=i
    print("maximum num is :" , max_num)
    print("minimum num is :" , min_num)
numbers()

    
       
