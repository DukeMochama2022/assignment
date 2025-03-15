my_list=[10, 20, 30, 40]

#inserting 15 at the second position
my_list.insert(1,15)

#extending anotherlist to my_list
another_list=[50,60,70]
my_list.extend(another_list)

#removing last element from the list
del my_list[-1]

# sorting my_list
my_list.sort()

#print index of value 30
index_30=my_list.index(30)
print(index_30)

print(my_list)