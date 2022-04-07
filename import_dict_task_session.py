#create dictionary
my_dict={1,"apple",2,"banana"}
print(my_dict)

#changing element in dictionary
my_dict={'first':'python','second':'java'}
my_dict['second']='c++'
my_dict['third']='sql'
print(my_dict)

#pop a dictionary
my_dict={'first':'python','second':'java','third':'c++'}
a=my_dict.pop('third')
print(a)

#clear a dict
my_dict={'first':'python','second':'java','third':'c++'}
b=my_dict.clear()
print(b)

#accesing a elements
my_dict={'first':'python','second':'java','third':'c++'}
print(my_dict['first'])
print(my_dict['third'])
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

