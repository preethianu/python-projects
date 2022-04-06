#find the size of tuple in python
import sys

tuple1=("a",1,"b",2,"c",3)
tuple2=("geeks","preethi","for","adhiti","geeks","meena")
tuple3=((1,"lion"),(2,"tiger"),(3,"cat"),(4,"wolf"))
print("size of tuple1:"+str(sys.getsizeof(tuple1))+"bytes")
print("size of tuple2:"+str(sys.getsizeof(tuple2))+"bytes")
print("size of tuple3:"+str(sys.getsizeof(tuple3))+"bytes")

#to find maximum and minimum k element in tuples
t=tuple()
n=int(input("total number of values in tuple"))
for i in range(n):
    a=input("enter elements")
    t=t+(a,)
    print("maximum value of tuple=",max(t))
    print("minimum value of tuple=",min(t))

#create a list of tuples from given list having number and its cube in each tuple
list=[1,2,5,6]
result=[(val,pow(val,3))for val in list]
print(result)

    
    
