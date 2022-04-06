#list
#program to swap first and last element of a list
def swaplist(list):
     start,*middle,end =list
     list=[end,*middle,start]

     return list
newlist=[12,35,9,56,24]
print(swaplist(newlist))

#program to swap two elements
def swapposition(list,ele1,ele2):

    list[ele1],list[ele2]=list[ele2],list[ele1]
    return list
list=[23,45,12,32,87,21]
ele1,ele2= 2,5
print(swapposition(list,ele1-1,ele2-1))

#way to find length of the list
a=[]
a.append("geeks")
a.append("for")
a.append("geeks")
print("the length of the list is:",len(a))

#clearing a list
list=[2,3,4,5,6]
print(list)
list.clear()
print(list)

#reversing a list using reverse()
def reverse(list1):
     list1.reverse()
     return list1
list1 =[2,3,4,5,6,7]
print(reverse(list1))

#python cloning or copying a list
def cloning(li1):
     li_copy=[]
     li_copy=li1.copy()
     return li_copy
li1=[2,4,6,7,8,9,10]
li2=cloning(li1)
print("original list:",li1)
print("after cloning:",li2)

#python program to find sum of element in the list
list1=[5,10,15,20]
total=0
for i in range(0,len(list1)):
     total=total+list1[i]
print("sum of all elements in given list: ",total)

#multiply all elements in the list
list1=[2,3,4]
result=1
for x in list1:
     result=result*x
print(result)
     
#to find smallest no in the list
list1=[10,20,30,4,50]
print("the smallest element in the list: ",min(list1))
#find largest no in the list
list1=[10,20,30,4,50]
print("the largest element in the list: ",max(list1))

#to find the second largest element in the list
list1=[10,20,30,4,50]
print("the second largest element in the list: ",list1[-3])

#to find N largest element in the list
l=[5,7,8,2]
n=int(input("enter the length of list: "))
for i in range(1,n+1):
     e=int(input("enter elment: "))
     l.append(e)
print(l)
l.sort()
print("the largest element of list is:",l[n-1])

#to print even no in the list
num=[]
n=int(input("enter number of list value: "))
for i in range(0,n):
     i=int(input("enter list element: "))
     num.append(i)
for i in num:
     if i%2==0:
          print(i,"is a even number ")
     else:
          print(i,"is a odd number")
     
#print all even number in given range
start,end =4,19
start=int(input("enter the start range:"))
end=int(input("enter the end range:"))
for i in range(start, end+1):
     if i%2==0:
        print(i,end=" ")

#print all odd numbers in given range
start,end=4,19
start=int(input("enter the start range:"))
end=int(input("enter the end range:"))
for i in range(start,end+1):
     if i%2!=0:
          print(i,end=" ")
          

#to print positive numbers in the list

list1= [2,4,-5,-6,8,-7]
for num in list1:
      if num>=0:
           print(num, end=" ")
#to print negative numbers in the list

list1=[2,4,-5,-6,8,-7]
for num in list1:
     if num<=0:
          print(num,end=" ")

#to print positive numbr range in list
start,end=-4,19
for num in range(start,end+1):
     if num>=0:
          print(num,end=" ")

#to print negative no in range
start,end=-4,19
for num in range(start,end+1):
     if num<0:
          print(num,end=" ")

#remove multiply elements from in a list
list=[20,21,17,18,23,50]
list=[i for i in list if i%2!=0]
print(list)

#remove empty list from the list
def remove(list):
     list=[4,5,[],3,[],[],9]
     print(remove(list))

#to find cumulative sum of a list
list1=[10,20,30,40,50]
list2=[]
sum=0
for i in range(0,list1):
     sum=sum+list1[i]
     list1.append(sum)
     print(list1)
      
#to print duplicates from a list of integers
li1=[4,2,3,1,1,2,3,4,5]
li2=set(li)
print(li2)
print(list(li2))

#count occurences of an element in a list
li3=[1,2,1,3,4,5,6,8,1,1]
print(li3.count(1))


 
 








                 
