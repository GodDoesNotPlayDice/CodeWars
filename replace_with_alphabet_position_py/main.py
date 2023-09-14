t = "2"
import string
import timeit

def alphabet_position(text):
    string = "abcdefghijklmnopqrstuvwxyz"
    text = text.replace(' ', '').replace("'",'').replace('.','').lower()
    return " ".join([str([i for i in string].index(i)+1) for i in text]) if text.isalpha() else "" # 0.0003024 ms

def alphabet_position_2(text):
    text = text.replace(' ', '').replace("'",'').replace('.','').lower()
    return " ".join([str([i for i in string.ascii_letters].index(i)+1) for i in text]) if text[0] in string.ascii_lowercase else ""

t1 = timeit.timeit(lambda: alphabet_position(t), number=1000)
t2 = timeit.timeit(lambda: alphabet_position_2(t), number=1000)

print(round(t1,8))
print(round(t2,8))
