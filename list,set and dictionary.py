Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#LIST
#Create an empty list
li1=[]
print(li1)
[]
print(type(li1))
<class 'list'>
li2=list()
print(li2)
[]
print(type(li2))
<class 'list'>

#TASK2
#Concatenate with[5,6,7,8]
li1=[5,6,7,8]
li2=[5,6,7,8]
li3=li2 + li1
print(li3)
[5, 6, 7, 8, 5, 6, 7, 8]

#task 3
#add 8,9,1,5,6,7,8,1 elements to the list
li1=[8,9,1,5,6,7,8,1]
li1.append(8)
li1.append(9)
li1.append(1)
li1.append(5)
li1.append(6)
li1.append(7)
li1.append(8)
li1.append(1)
print(li1)
[8, 9, 1, 5, 6, 7, 8, 1, 8, 9, 1, 5, 6, 7, 8, 1]

#task4
#find the frequency of 8 count
li1=[2,3,4,8,4,5,2,8,1]
print(li1.count(8))
2

#task5
#find the mean of the list
li1=[3,4,1,2]
li2=sum(li1)/len(li1)
print(li2)
2.5

#task6
#find sum (list)+min+max
li1=[2,3,4,6,7]
li2=sum(li1)
li3=min(li1)
li4=max(li1)
li5=li2+li3+li4
print(li5)
31

#task7
#find median of the list
li1=[1,2,3,4,5,6,7,8]
median=len(li1)/2
print(li1)
[1, 2, 3, 4, 5, 6, 7, 8]
print(round(median))
4

#task8
#remove duplicates from the list and give output in the format of tuple
li1={1,2,3,4,5,6,7,8}
li2=tuple(li1)
print(li2)
(1, 2, 3, 4, 5, 6, 7, 8)


#tuple
#task1
#create two tuples
li1=(1,4,5,6,7,8)(5,6,7,8,9)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    li1=(1,4,5,6,7,8)(5,6,7,8,9)
TypeError: 'tuple' object is not callable
li2=(5,6,7,8,9)
a=li1+li2
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a=li1+li2
TypeError: unsupported operand type(s) for +: 'set' and 'tuple'
a=li1 + li2
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a=li1 + li2
TypeError: unsupported operand type(s) for +: 'set' and 'tuple'
li1=(1,4,5,6,7,8)
li2=(5,6,7,8,9)
a=li1 + li2
print(a)
(1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9)
print(li1)
(1, 4, 5, 6, 7, 8)
print(li2)
(5, 6, 7, 8, 9)

#task2
#find common elements between two tuples
tpl1=(4,'v',(1,3),9,8,('m','v'))
tpl2=(7,6,(3,1),5,9,('m','v'))
tpl1_set=set(tpl1)
tpl2_set=set(tpl2)
common_element=(tpl1_set & tpl2_set)
print(common_element)
{9, ('m', 'v')}

#task3
#find the index value of 9(after concatention
tupl1=(1,4,5,6,7,8)
tupl2=(5,6,7,8,9)
tupl3=tupl2 + tupl1
print(tupl3)
(5, 6, 7, 8, 9, 1, 4, 5, 6, 7, 8)
print(tupl3.index(9))
4
#task3
#multiply above elements  3 times
print(tupl3*3)
(5, 6, 7, 8, 9, 1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9, 1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9, 1, 4, 5, 6, 7, 8)

#task5

#set
#task1
#create two empty sets
set1=set()
print(set1)
set()
print(type(set1))
<class 'set'>

set2=set()
print(set2)
set()
print(type(set2))
<class 'set'>
#task3
#task2
#update set1 with 7,8,9,1,2,3,4,5,0
set1={7,8,9,1,2,3,4,5,0}
set.update(set1)
print(set)
<class 'set'>
print(set1)
{0, 1, 2, 3, 4, 5, 7, 8, 9}

#task3
#update set2 with 4,5,6,0
set1={4,5,6,0}
set.update(set2)
print(set1)
{0, 4, 5, 6}

#task4
#check whether set2 is subset of set1 or no?
print(set1.issubset(set))
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    print(set1.issubset(set))
TypeError: 'type' object is not iterable
set1=(7,8,9,1,2,3,4,5)
print(set1.subset(set))
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    print(set1.subset(set))
AttributeError: 'tuple' object has no attribute 'subset'
print(set.subset(set1))
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    print(set.subset(set1))
AttributeError: type object 'set' has no attribute 'subset'. Did you mean: 'issubset'?
set1=(7,8,9,1,2,3,4,5)
set2=(4,5,6,0)
print(set2.issubset(set1))
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    print(set2.issubset(set1))
AttributeError: 'tuple' object has no attribute 'issubset'
set1={7,8,9,1,2,3,4,5}set2=(4,5,6,0)
SyntaxError: invalid syntax
set2={4,5,6,0}
print(set2.issubset(set1))
False

#task5
#remove 8 from set1 and set2 ==>find the inferences
set1={7,8,9,1,2,3,4,5}
set2={4,5,6,0}
set1.remove(8)
print(set1)
{1, 2, 3, 4, 5, 7, 9}
set2.remove(8)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    set2.remove(8)
KeyError: 8
#discard 0 from set1 and set2
set1.discard(0)
print(set1)
{1, 2, 3, 4, 5, 7, 9}
set2.discard(0)
print(set2)
{4, 5, 6}

#task7
#find collection of both sets
set1={7,8,9,1,2,3,4,5,0}
set2={4,5,6,0}
set1.update(set2)
print(set1)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
set2.update(set1)
print(set2)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

#task8
#check whether both have common elements are no?
set1={7,8,9,1,2,3,4,5,0}
set2={4,5,6,0}
print(set1.isdisjoint(set2))
False


#dictionary
#create a dictionary
dict={1:[""english"",""maths"",""science""],2:[10,20,30],3:[""bio-botany"",""bio-zoology"",""algebra""]}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
dict={1:[""english"",""maths"",""science""],2:[10,20,30],3:[""bio-botany"",""bio-zoology"",""algebra""]}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
dict={1:["english"",""maths"",""science""],2:[10,20,30],3:[""bio-botany"",""bio-zoology"",""algebra""]}
         
SyntaxError: unterminated string literal (detected at line 1)
dict={1:["english","maths","science"],2:[10,20,30],3:["bio-botany","bio-zoology","algebra"]}
         
dict={1:["english","maths","science"],2:[10,20,30],3:["bio-botany","bio-zoology","algebra"]}
         
print(dict)
         
{1: ['english', 'maths', 'science'], 2: [10, 20, 30], 3: ['bio-botany', 'bio-zoology', 'algebra']}

#task2
         
#extract "bobtn" from above dictionary
         
print(dict["bobtn"])
         
Traceback (most recent call last):
  File "<pyshell#176>", line 1, in <module>
    print(dict["bobtn"])
KeyError: 'bobtn'

#task3
         
#extract "arbeg" from above dictionary
         
print(dict["arbeg"])
         
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    print(dict["arbeg"])
KeyError: 'arbeg'
print(dict.keys())
         
dict_keys([1, 2, 3])
tup=tuple(dict.items())
         
print(type(tup))
         
<class 'tuple'>

#task4
         
#find the average of all numbers available
         
#find the average of all numbers available under key ""2""
         
values=dict[2]
         
print(values)
         
[10, 20, 30]
avg=sum(values)/len(values)
         
print(avg)
         
20.0
