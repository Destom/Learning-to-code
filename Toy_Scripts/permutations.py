from itertools import permutations
stuff = [0, 1, 2, 3, 4]
Count =0
for i in range(0, len(stuff)+1):
    for subset in permutations(stuff, i):
        print(subset)
        Count+=1
print (Count)