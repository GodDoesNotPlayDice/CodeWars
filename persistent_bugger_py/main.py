import timeit
num = 999
def persistence(n):
    n = str(n)
    count = 0
    if len(n) == 1:
        return 0
    else:
        while len(n) > 1:
            count += 1
            ax = "*".join([i for i in n])
            n = str(eval(ax))
    return count
    
t1 = timeit.timeit(lambda: persistence(num), number=1000)
print(round(t1,3))
print(persistence(num))