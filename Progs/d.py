'''def cal_ar(b,h):
    a = (1/2)*b*h
    return a

b=2
h=4
print(cal_ar(b,h))'''

def f(d, key):
    if key in d:
        return d[key]
    else:
        return 'No value found'
week = {1:'mon', 2:'tue', 3:'wed', 4:'thur', 5:'fri', 6:'sat', 7:'sun'}
print(f(week, 5))
print(f(week, 10))
