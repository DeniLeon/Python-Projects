#la suma de dos indices distintos en una lista deben dar un target, complejidad en O(n) mejorada de O(n^2)

def twosum(num,target):
    visto = {}

    for i,x in enumerate(num):
        complemento= target-x

        if complemento in visto:
            return [visto[complemento], i]

        visto [x]=i


num=[1,3,5,6]
target=8
print(twosum(num,target))