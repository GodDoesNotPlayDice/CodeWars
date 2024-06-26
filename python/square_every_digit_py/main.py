import timeit
n = 9119
def square_digits(num):
    return int(''.join([str(int(i)**2) for i in str(num)]))
print(square_digits(n))

t1 = timeit.timeit(lambda: square_digits(n), number=1000)
t1 = round(t1, 3)
print(t1) 