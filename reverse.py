''' write a program to find the reverse of given no'''


def reverse(num):
    rev=0
    while num>0:
        rev=rev*10+num%10
        num//=10
    return rev


def isPalindrome(num):
   return num==reverse(num)

print(reverse(1219))
print(isPalindrome((121)))

print(reverse(123))
print(isPalindrome((123)))

def getPalindrome(start,end):

    for i in range(1,end+1):
        if isPalindrome(i):
            res=res+str(i)+","
    return res

print(getPalindrome(1,1000))

