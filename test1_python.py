#1.python program to check if string contain only defined characters using regex
import re
def check(str,pattern):
    if re.search(pattern,str):
        print("valid string")
    else:
        print("invalid string")
pattern = re.compile('^[1234]+$')
check('2134',pattern)
check('349',pattern)

#2.python program to count uppercase,lowercase,special character and numeric values using regex
import re
string ="this is geeksforgeeks !,123"
#creating seprate list using
#the re.findall()method
uppercase_characters=re.findall(r"[A-Z]",string)
lowercase_characters=re.findall(r"[a-z]",string)
numerical_characters=re.findall(r"[0-9]",string)
special_characters=re.findall(r"[, .!?]",string)

print("the no of uppercase characters is",len(uppercase_characters))
print("the no of lowercase characters is ",len(lowercase_characters))
print("the no of numerical characters is ",len(numerical_characters))
print("the no of special characters is ",len(special_characters))

#python program to put spces betwn words starting with capital letters using regex
import re

def putspcae(input):
    #regex[A-Z][a-z]* means any string starting
    #with capital char foll by many
    #lowercase letters
    words=re.findall('[A-Z][a-z]*',input)

    #change first letter of each wor into lower
    #case
    for i in range(0,len(words)):
        words[i]=words[i][0].lower()+words[i][1:]
    print(' '.join(words))
    
#4.diff ways to clear a list in python
li7=[1,2,5,3]
li7.clear()
print(li7)

#reversing a list
li8=[1,2,-4,2,-5,3,28]
li8.reverse()
print(li8)
#6.python program to find sum of elements in list
li9=[1,2,3,4]
print(sum(li9))

#7.multiply all numbers in the list
li10=[1,2,3,5]
print(li10[0]*li10[1]*li10[2]*li10[3])
#8.program to find smallest no in the list
li11=[1,2,3,4]
print(min(li11))
#9.to find laragest no in the list
li12=[1,4,5,3,55]
print(max(li12))
#10.to find second largest no in the list
li13=[5,10,20,40,30,7,60]
li13.sort()
print(li13)
print(li13[-2])
#11.prg to find N largest elements from a list
li14=[2,-3,10,30,40,25]
li14.sort()
print(li14)
print(li14[-4:])
#12.to print even no in a list
li15=[2,3,4,5,6,8]
li16=[]
for i in li15:
    if i % 2==0:
        li16.append(i)
        print(li16)
#13.python pgm to print odd no in the list
li17=[2,3,5,8,10,12]
li18=[]
for x in li17:
    if x%2==1:
        li18.append(x)
        print(li18)

#14.pgm to print all even numbers in a range
s1=4
e1=15
for i1 in range(s1,e1):
    if i1 % 2 ==0:
        print(i1,end=",")

#15.print all odd no in range
s2=4
e2=15
for i2 in range(s2-1,e2+1):
    if i2%2 ==1:
        print(i2)
#to print positive no in a list
li19=[2,3,5,-1,-3,-6]
for pos in li19:
    if pos>0:
        print(pos)
#to print neg no in the list
li20=[-2,-4,4,2]
for neg in li20:
    if neg<0:
        print(neg)
#to print all positive no in range
s3=-8
e3=6
for positive in range(s3,e3):
    if positive>0:
         print(positive)
#19.python pgm to print all negative no in range:
s4=-10
e4=8
for negative in range(s4,e4):
    if negative<0:
        print(negative)
        
#20.remove multple elements from a list in python
li21=[2,3,4,6]
li21.remove(2)
print(list(li21))

#21.remove empty list from list
li22=[3,4,[],5,[],6,[]]
print(str(li22))
li23=list(filter(None,li22))
print(list(li23))

#22.find factoril of a number without using function(for loop)
num=int(input("enter the factorial number:"))
fact=1
if num<0:
    print("not eligible for negative numbers")
else:
    for k in range(1,num+1):
        fact=fact*k
print("factorial number is ",fact)

#23.find factorial of a number without using fun(while loop)
no=int(input("enter the number:"))
fact=no
while no>1:
    no=no -1
    fact=fact*no
print(fact)
#24.fibonacci series
def Fibonacci(n):
    if n<0:
        print("incorrect input")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(9))
#25.identify middle character of the string
str1=input("enter the word:")
middle_character=(len(str1)//2)
print(str1[middle_character])
         
