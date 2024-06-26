import timeit

def descending_order(num):
    arr, new_arr, count = [int(i) for i in [i for i in str(num)]], [], 0
    l = len(arr)
    while count < l:
        nmax = max(arr)
        arr.pop(arr.index(nmax))
        new_arr.append(nmax)
        count += 1
    return int(''.join([str(i) for i in new_arr]))
t1 = timeit.timeit(lambda: descending_order(123456789), number=1000)
t1 = round(t1, 3)
print(t1) # Time 0.01ms