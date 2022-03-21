Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#task1
a=input("enter the string:")
enter the string:python
count=len(a)//2
count=len(a)
middle_char=count//2
print(a[middle_char])
h
#task2
str1="****python********"
str2="**python*************"
str3="********java************"
print(str1.strip("*"))
python
print(str2.rstrip("*"))
**python
print(str3.lstrip("*"))
java************
#task3
#collect three string from user
x=input("enter the name and value:")
enter the name and value:ravi 10.30
y=input("enter the name and value:")
enter the name and value:meghala 12.19
z=input("enter the name and value:")
enter the name and value:gokul 20.20
x=x.split()
y=y.split()
z=z.split()
print(float(x[1])+float(y[1])+float(z[1]))
42.69
#task 4
#collect two string from user
s1=input("enter the 1st string:")
enter the 1st string:python
s2=input("enter the 2nd string:")
enter the 2nd string:java
c1=len(s1)
c2=len(s2)
mid=c1/2
mid=c2/2
x=s2[0]+s1[1:]+s1[0]+s2[1:]+str(c1)+str(c2)+s1[mid]+s2[mid]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    x=s2[0]+s1[1:]+s1[0]+s2[1:]+str(c1)+str(c2)+s1[mid]+s2[mid]
TypeError: string indices must be integers
s1=input("enter the 1st string:")
enter the 1st string:python
s2=input("enter the 2nd string:")
enter the 2nd string:java
c1=len(s1)
c2=len(s2)
mid1=c1/2
mid2=c2/2
x=s2[0]+s1[1:]+s1[0]+s2[1:]+str(c1)+str(c2)+s1[mid1]+s2[mid2]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    x=s2[0]+s1[1:]+s1[0]+s2[1:]+str(c1)+str(c2)+s1[mid1]+s2[mid2]
TypeError: string indices must be integers
c1=len(s1)
c2=len(s2)
mid1=c1//2
mid2=c2//2
x=s2[0]+s1[1:]+s1[0]+s2[1:]+str(c1)+str(c2)+s1[mid1]+s2[mid2]
print(x)
jythonpava64hv
#task5
#string 1:maths
#string 2:science
a=input("enter the subject name:")
enter the subject name:maths
b=input("enter the subject name:")
enter the subject name:science
c1=len(a)
c2=len(b)
mid1=c1//2
mid2=c2//2
x=s2[0]+s1[1:]+s1[0]+s2[1:]+str(c1)+str(c2)+a[mid1]+b[mid2]
print(x)
jythonpava57te
x=a[0]+b[1:]+b[0]+a[1:]+str(c1)+str(c2)+a[mid1]+b[mid2]
print(x)
mciencesaths57te


#task6
#string1=wikipedia
#string2=typescript
a="wikipedia"
b="typescript"
a=input("enter the 1st word:")
enter the 1st word:wikipedia
b=input("enter the second word:")
enter the second word:typescript
c1=len(a)
c2=len(b)
mid1=c1//2
mid2=c2//2
x=a[mid1]
y=b[mid2]
total=ord(x)+ord(y)
z=""ascii value of ""+ x +"" - ""+ str(ord(x))+ "" + "" +""ascii value of ""+ y +"" - "" + str(ord(y))+ "" = "" +str(total)
SyntaxError: invalid syntax
z= ""Ascii value of "" + x +"" - ""+ str(ord(x))+ "" + "" + ""Ascii value of "" + y +"" - "" + str(ord(y))+ "" = "" +str(total)
SyntaxError: invalid syntax
total=ord(x) + ord(y)z= ""Ascii value of "" + x +"" - ""+ str(ord(x))+ "" + "" + ""Ascii value of "" + y +"" - "" + str(ord(y))+ "" = "" +str(total)
SyntaxError: invalid syntax
total=ord(x)+ord(y)
z= ""Ascii value of "" + x +"" - ""+ str(ord(x))+ "" + "" + ""Ascii value of "" + y +"" - "" + str(ord(y))+ "" = "" +str(total)
SyntaxError: invalid syntax
total = ord(x) + ord(y)
result= "Ascii value of "" + x +"" - ""+ str(ord(x))+ "" + "" + ""Ascii value of "" + y + "" - "" + str(ord(y))+ "" = "" +str(total)
SyntaxError: unterminated string literal (detected at line 1)
result= "Ascii value of "" + x +"" - ""+ str(ord(x))+ "" + "" + ""Ascii value of "" + y + "" - "" + str(ord(y))+ "" = "" +str(total)""
SyntaxError: unterminated string literal (detected at line 1)


#task7
string=computer
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    string=computer
NameError: name 'computer' is not defined. Did you mean: 'compile'?
string="computer"
a=input("enter the string:")
enter the string:computer
c=len(a)
first_str=a[0]
last_str=a[c-1]
print(first_str+str(c)+last_str)
c8r
first_str=a[0]
last_str=a[c-2]
print(first_str+str(c)+last_str)
c8e


#task8
a=input("enter the word:")
enter the word:programming
c=len(a)
first_str=a[0]
last_str=a[c-1]
print(first_str+str(c)+last[str])
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    print(first_str+str(c)+last[str])
NameError: name 'last' is not defined. Did you mean: 'list'?
print(first_str+str(c)+last_str)
p11g


#task9
#say hello world with python
a="hello world!"
print(a)
hello world!

#task 10
#swap case
a=input("enter the name:")
enter the name:"mY namE IS PREEthi"
print(a.swapcase())
"My NAMe is preeTHI"


#task 11
#what is your name
first_name=input()
hello ross
last_name=input()
taylor
print(f" {first_name} {second_name} ! you just deloved in python")
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    print(f" {first_name} {second_name} ! you just deloved in python")
NameError: name 'second_name' is not defined
print(f" {first_name} {last_name} ! you just deloved in python")
 hello ross taylor ! you just deloved in python

#task12
 
#mutation
 
a=input()
asdferhi
string=a[:3]+k+a[3:]
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    string=a[:3]+k+a[3:]
NameError: name 'k' is not defined
string=a[:3]+f+a[3:]
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    string=a[:3]+f+a[3:]
NameError: name 'f' is not defined
string=a[:3]+k+a[4:]
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    string=a[:3]+k+a[4:]
NameError: name 'k' is not defined
asdfghj1
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    asdfghj1
NameError: name 'asdfghj1' is not defined
a=input()
asdfghj1
string=a[:3]+k+a[4:]
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    string=a[:3]+k+a[4:]
NameError: name 'k' is not defined
string=a[:3]+"k"+a[4:]
print(string)
asdkghj1


#task11
#arithmetic operator
x=5
y=6
print(x+y)
11
print(x*y)
30

#task12
#python division
a=7
b=3
print(a//b)
2
print(a/b)
2.3333333333333335
