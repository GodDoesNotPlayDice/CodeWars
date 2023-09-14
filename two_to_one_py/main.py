import timeit
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
def longest(a1, a2):
    l = sorted(a1+a2)
    for i in l:
        while l.count(i) > 1:
            l.remove(i)
    return "".join(l)
print(longest(a, b))
t1 = timeit.timeit(lambda: longest(a, b), number=1000)
t1 = round(t1, 3)
print(t1) #0.013ms