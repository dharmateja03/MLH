#sorting a list
print("Enter the number of elements")
n=int(input())  #number of elements
print("enter the elements")
l=list(map(int,input().split()))
l.sort() #inbuilt function
print(*l) #prints every element l seprated by space
