f = open("ex.txt")
print(f.read())
f.close()

with open("ex.txt") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())