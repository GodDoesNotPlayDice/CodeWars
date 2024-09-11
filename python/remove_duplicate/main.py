def solve(arr):
    clean = set(arr)
    n_arr =[i for i in clean if i in clean]
    return n_arr
print(solve([3, 4, 4, 3, 6, 3]))
