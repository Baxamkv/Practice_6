lst = [5,6,2]
lst2 = ['a','b','c']

for i, j in enumerate(lst):
    print(f"{j} : {i}")


for i, j in zip(lst, lst2):
    print(f"{i} : {j}")


