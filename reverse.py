''' write a program to find the reverse of given no'''
num=int(input("enter a no:"))
rev=0
while num>0:
    rev=rev*10+num%10
    num//=10
print("rev num is:",rev)
