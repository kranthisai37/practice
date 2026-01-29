''' write a program to find the reverse of given no'''


def reverse(num):
    rev=0
    while num>0:
        rev=rev*10+num%10
        num//=10
    return rev


def isPalindrome(num):
   return num==reverse(num)

print(reverse(121))
print(isPalindrome((121)))

print(reverse(123))
print(isPalindrome((123)))

def getPalindrome(start,end):
<<<<<<< HEAD
    res=""
=======
    res==""
>>>>>>> b1d4c5dd86c84d7ab8ea24d92ed50439aea406f1
    for i in range(1,end+1):
        if isPalindrome(i):
            res=res+str(i)+","
    return res

print(getPalindrome(1,1000))
<<<<<<< HEAD




=======
>>>>>>> b1d4c5dd86c84d7ab8ea24d92ed50439aea406f1
