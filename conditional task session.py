#task1
#fizz buzz
#get one number from user
#multiple of 3 ==>fizz
#multiple of 5 ==>buzz
#multiple of 3 and 5 ==>fizzbuzz
fizzbuzz=int(input())
for fizzbuzz in range(31):
    if fizzbuzz%3 ==0 and fizzbuzz%5 ==0:
        print("fizzbuzz")
        continue
    elif fizzbuzz %3 ==0:
        print("fizz")
        continue
    elif fizzbuzz %5 ==0:
        print("buzz")
        continue
print(fizzbuzz)

#task2
#get oe mark from student
#mark 0 to 100valid otherwise invalid mark
print("enter marks obtained in 5 sujects:")
markone=int(input())
marktwo=int(input())
markthree=int(input())
markfour=int(input())
markfive=int(input())

total=markone+marktwo+markthree+markfour+markfive
avg=total/5
if avg>=91 and avg<=100:
    print("grade A")
elif avg>=81 and avg<=91:
    print("grade B")
elif avg>=71 and avg<=81:
    print("grade C")
elif avg>=61 and avg<=71:
    print("grade D")
elif avg>=51 and avg<=61:
    print("grade E")
else:
    print("invalid mark!")


#task3
#loop
#using range function print multiples of 5 from 0 to 75
#using range function print multiples of 8 from 0 to 72
    print("multiples of five:")
for i in range (0,75):
    if i%5==0:
        print(f'{i}:multiples of five')
    else:
        print(f'{i}:not multiples of five')

#using range function print multiples of 8 from 0 to 72
        print("multiples of eight:")
for i in range (0,72):
    if i%8==0:
        print(f'{i}:multiples of eight')
    else:
        print(f'{i}:not multiples of eight')

#task4
#using range function print multiples of 5 from 75 to 0
#using range function print multiples of 8 from 96 to 72
        print("multiples of five:")
for i in range (75,0):
    if i%5==0:
        print(f'{i}:multiples of five')
    else:
        print(f'{i}:not multiples of five')
        
#using range function print multiples of 8 from 96 to 72
       
for i in range (96,72)
    if i%8==0:
        print(f'{i}:multiples of eight')
    else:
        print(f'{i}: not multiples of eight')


#get a dynamic list from user
        lst=[0,1,2,3,4]
        n=int(input("enter no of elements:"))
for i in range(0,5):
         ele =[input(),int(input())]
         lst.append(ele)
         print(lst)
#task2 and task3
#get no of elements from user
#loop through range
#append to list/dicti
       print("enter no of elements from user:")
       dict={0,1,2,3,4,5,6,7}
       list
        
        
    
    
    
