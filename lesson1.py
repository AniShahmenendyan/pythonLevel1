'''Variables'''

x = 5
y = 6.5
s = 'STRING'
b = True

print(type(x))

x = int(5)

a = 1
b = a

print(id(a))
print(id(b))

del a
print(id(b))

int(5.6)
s1 = 'hello'
s2 = "hello"

print(id(s1))
print(id(s2))

a = b = c = 13

x, y = 4, 6
print(x)
print(y)

bool(False)
bool(0)
bool('')
bool([])
bool(())
bool({})
bool(None)

print(12 < 13)
print(bool([1, 2, 4]))

'''List'''

lst = [1, 2, 3, 5, 2]
lst_1 = list()

lst.append(12)

print(lst)
print(lst.index(12))

removed_obj = lst.pop()
print(removed_obj)

print(lst[1:4])
print(lst[1:5:2])

lst.sort(reverse=True)
print(lst)

lst_2 = lst.copy()

lst_3 = [1, 3, 5, [1, 4, 6]]
lst_4 = lst_3.copy()

a = [1, 4, 6]
b = [1, 4, 6]

# https://www.w3schools.com/python/python_lists_methods.asp

'''String'''

a = 'Hello world!!!'
print(a[0:4])

splited_str = a.split(' ')
print(splited_str)

print(' '.join(splited_str))

# a = 3
# str_a = str(a)
# print(a.__str__())
print(a.upper())

# print('str' is 'STR')

x = 1
y = 3
x_eval = 'x is {1} and y = {0}'.format(x, y)
x_eval = f'x is {x + 1} and y = {y + 1}'
p = 4.298632483927432
print('p is {:.5f}'.format(p))

print(r'hello \n world!!!')

print('home' in 'sleep in home ')

str_1 = 'home'
print(str_1[0])
# str_1[0] = 'H'

''' tuple '''

t = (1, 3, 4)
t_1 = tuple()

# lst = list(t)
# lst.append(5)
# t3 = tuple(lst)
# print(t3)

print(t.count(1))
print(t.index(1))

a = t[0]
b = t[1]
c = t[2]

a, b, c = t

'''Set'''

st = {1, 2, 4}
st1 = set()

print(st)
st_2 = {1, 2, 7}

print(st.union(st_2))
print(st.intersection(st_2))

print(st - st_2)

st.discard(2)
# st.remove(2)
print(st)
print(st | st_2)

'''dict'''

d = dict()
d = {'key1': 1, 'key2': 3, 'key3': 7}

print(hash('key1'))
print(hash('key1'))
print(hash('key1'))
print(hash('key1'))

# print(d['key4'])
# print(d.get('key4', 'error'))

print(d.values())
print(d.keys())
print(d.items())

# k,v = (1, 3)

for k, v in d.items():
    if v == 1:
        print('this is 1 value, key is {}'.format(k))

d.update({'key4': 9})
print(d)
del d['key4']
print(d)

lst = list(range(50))
print(lst)

lst_1 = []
for i in lst:
    if i % 2 != 0:
        lst_1.append(i)

print(lst_1)

lst_2 = [ i if i %2 != 0 else i *2 for i in lst]
print(lst_2)

dct_2 = {str(k) + '__':v *2 for k,v in d.items()}
print(d)
print(dct_2)

a = 10
if a > 2:
    print('a>2')
else:
    print('a<=2')

print('a>2' if a > 2 else 'a<=2')


import time
rng_list = list(range(53))

lst = []
start_time_for = time.time()
for i in rng_list:
    lst.append(i)
print('time for = {}'.format(time.time() - start_time_for))


start_time_while = time.time()
lst = []
i = 0
while i < len(rng_list):
    lst.append(i)
    i += 1

print('time while = {}'.format(time.time() - start_time_while))

for i in rng_list:
    print(i)
    if i == 55:
        break
else:
    print('for is not broken')


found = False
for i in rng_list:
    if i == 55:
        found = True
if not found:
    print('for is not broken')