lst = [5,6,2,15,7,8,5,3]
lst = list(map(lambda x: x*3, lst))

print(lst)

lst = list(filter(lambda x: True if x % 2 == 0 else False, lst))

print(lst)

