with open("test1.txt", "r") as f:
    lst = [(int(i), int(i)**2) for i in f.read().split(' ') if int(i) % 2 == 0]
print(lst)