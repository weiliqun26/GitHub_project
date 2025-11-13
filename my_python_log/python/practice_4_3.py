list = []
for i in range(1, 21):
    list.append(i)
print(list)
list2 = [num for num in range(1, 21)]
print(list2)


list3 = []
for i in range(1, 1000001):
    list3.append(i)
# print(list3)

print(min(list3))


print(max(list3))

print(sum(list3))

list4 = []
for i in range(1, 21, 2):
    list4.append(i)
print(list4)

list5 = [num for num in range(3, 31, 3)]
print(list5)


for i in range(1, 11):
    i = i**3
    print(i)

list6 = [value**3 for value in range(1, 11)]
print(list6)
print(f"the first three items in the list are:{list6[ :3]}")
print(f"the middle three items in the list are:{list6[4:7]}")
print(f"the last three items in the list are:{list6[-3:]}")
