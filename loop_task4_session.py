#task4
#get two integers from user
#print multiples of 8 between them
#input 10 to 100
#multiples of 8
x=int(input("enter the two integers:"))
for i in range (10,100):
      if i%8==0:
             print(f'{i}:multiples of eight')
      else:
             print(f'{i}:not multiples of eight')

#task5
#input=[3,4,5,2,7,8,9,10]
#output
li1=[3,4,5,2,7,8,9,10]
for i in li1:
    if i%2==0:
        print(f'{i}:even')
    else:
        print(f'{i}:odd')

#task6
#input=[-1,-7,8,10,20,21,17,28,-3,0,0,]
li1=[-1,-7,8,10,20,21,17,28,-3,0,0]
li_pos=[]
li_neg=[]
li_zeros=[]
for i in li1:
      if i>0:
         li_pos.append(i)
      elif i<0:
         li_neg.append(i)
      elif i==0:
         li_zeros.append(i)
print(li_pos)
print(li_neg)
print(li_zeros)
#task3
#get a dynamic dictionary from user
dyn={}
ele=int(input("enter the number of elements:"))
for i in range(0,ele):
      key=int(input("enter a key  "))
      value=input("enter a value  ")
      dyn[key]=value
      print(dyn)
      
      
#task2
#get a dynamic list from user

lst=[]
ele=int(input("enter the number of elements  "))
for i in range(0,ele):
      user=int(input("enter the elements in the list:  "))
      lst.append(user)
      print(lst)
      
      
      

      
          
       
