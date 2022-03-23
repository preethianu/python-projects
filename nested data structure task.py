Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
li1=[2,3,4,5,[45,56,67,78,[111,222,333,[5555,3333,[10000,50000,"python","computer"],1111,7777,8888],444,555,666,777],89,23,34]]
print(li1[3])
5

print(li1[4][1])
56
print(li1[4][4][1])
222
print(li1[4][4][3][2][1])
50000
print(li1[4][4]3][2][3][3:6])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('

print(li1[4][4][3][2][3][3:6])
put
print(li1[4][4][3][4])
7777
print(li1[4][4][6])
666
print(li[4][5])
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(li[4][5])
NameError: name 'li' is not defined. Did you mean: 'li1'?
print(li1[4][5])
89
print(li1[4][4][3][2][2][4:])
on
print(li1[4][4][3][2][2][4:])
on
print(li1[4][4][2])
333
print(li1[4][4][3][1])
3333

#task2
a=[1,2,3,4,[100,101,102,"computer_science"],200,203]

print(a[4][3][:8])
computer
print(a[4][3][9:])
science

#task3
a=[1,2,3,4,[101,102,103,[201,202,[999]],666,777]]
print(a[4][4])
666
print(a[4][1])
102
print(a[4][7])
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(a[4][7])
IndexError: list index out of range
print(a[4][6])
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(a[4][6])
IndexError: list index out of range
print(a[4][3][2])
[999]

#task4
li1=[2,3,""python"",""hello"",4,5,0]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
li1=[2,3,"python","hello",4,5,0]
print(li1[3][2:4])
ll
print(li1[2][2:6])
thon

#task5
li1=[1,2,3,4,5,[11,22,33,44,55,[111,222,333,444],6666,7777],7777]
print(li1[5][0])
11
print(li1[5][6])
6666
print(li1[5][-2])
6666
print(li1[5][7])
7777
print(li1[6])
7777
print(li1[5][5][1])
222
print(li1[-2][-1])
7777
print(li1[-2][2:4])
[33, 44]


#task6
a={1:[1,2,3,"python"],2:{10:"hllo",20:"welcome",40:"science"},99:{3,4,5,6},40:{1:"zoology",2:"botany"}}
print(a[1]3][0:2])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
print(a[1][3][0:2])
py
print(a[2][10][1:5])
llo
print(a[2][40][3:5])
en
print(a[40][1][0:3])
zoo
print(a[40][2][0:3])
bot


#task7
#convert below one to tuple
li1=[5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
tup=tupl(li1)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    tup=tupl(li1)
NameError: name 'tupl' is not defined. Did you mean: 'tuple'?
tup=tuple(li1))
SyntaxError: unmatched ')'
tup=tuple(li1)
print(tup)
(5, 4, 3, 6, 2, 7, 1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 5)


#task8
#remove duplicates from below list
a=[5,4,3,6,2,7,1,2,3,4,1,2,3,4,5,6,5]
a=set(a)
print(a)
{1, 2, 3, 4, 5, 6, 7}

#task9
#convert below set into a list
a={5,4,3,6,2,7,1}
print(a)
{1, 2, 3, 4, 5, 6, 7}
print(type(a))
<class 'set'>
b=list(a)
[1,2,3,4,5,6,7]
[1, 2, 3, 4, 5, 6, 7]
print(type(b))
<class 'list'>


#task10
#convert below two lists into dictionary
a=[1,2,3,4,5]
b=["python","cpp","c","java","php"]
x=str(a)
y=str(b)
result=dict(zip(a,b))
print(result)
{1: 'python', 2: 'cpp', 3: 'c', 4: 'java', 5: 'php'}
