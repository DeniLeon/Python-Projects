#la suma de dos indices distintos en una lista deben dar un target, complejidad en O(n2)

def twosum(num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i] + num[j] == target:
                return [i,j]


num=[1,5,3,4]
target=9
print(twosum(num,target))