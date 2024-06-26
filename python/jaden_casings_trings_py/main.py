import timeit
a = "How can mirrors be real if our eyes aren't real"
def to_jaden_case(text):
    return " ".join([i.capitalize() for i in text.split()])
print(to_jaden_case(a))
t1 = timeit.timeit(lambda: to_jaden_case(a), number=1000)
t1 = round(t1, 3)
print(t1) # 0.003 ms

# Stop Watch 2 min
