# Accessing set member
j = {10, 20, 30, 40, 50, 60, 70, 80, 90}
print(j)

# i = {10, 20, 30, 40, 50, 60, 70, 80, 90}
# for number in i:
#     print(i)

# check values
names = {'om', 'arjun', 'karan', 'satish', 'jay' }
print('ramesh' in names)

names = {'om', 'arjun', 'karan', 'satish', 'jay' }
print('ramesh' not in names)

# Add item in set
names = {'om', 'arjun', 'karan', 'satish', 'jay' }
names.add('ramesh')
print(names)

# check length of set
names = {'om', 'arjun', 'karan', 'satish', 'jay' }
print(len(names))

# delete set
names = {'om', 'arjun', 'karan', 'satish', 'jay' }
del names


# union() method of set
i = {1,2,3,4,5}
j = {6,7,8,9,10}
values = i.union(j)
print(values)

# intersection of set
i = {1,2,3,4,5,7,9}
j = {5,4,6,7,8,9,10}
add = i & j
print(add)

# Difference of set
i = {1,2,3,4,5,7,9}
j = {5,4,6,7,8,9,10}
diff = i - j
print(diff)

