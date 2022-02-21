'''Python References'''
import ctypes

counter = 100
print(id(counter))
print(hex(id(counter)))

max = counter
print(id(max))
print(hex(id(max)))


def ref_count(address):
    return ctypes.c_long.from_address(address).value


numbers = [1, 2, 3]
numbers_id = id(numbers)
print(ref_count(numbers_id))

ranks = numbers
print(ref_count(numbers_id))

ranks = None
print(ref_count(numbers_id))

'''garbage collector'''
import gc


def object_exist(object_id):
    for object in gc.get_objects():
        if id(object) == object_id:
            return True
    return False


print(object_exist(numbers_id))
numbers = None


class A():
    def __init__(self):
        self.b = B(self)


class B():
    def __init__(self, a):
        self.a = a


a_instance = A()
# print(a_instance.b)
# print(a_instance.b.a)
# print(a_instance.b.a.b.a.b.a.b.a)

# print(id(a_instance))
# print(id(a_instance.b.a))
# print(id(a_instance.b.a.b.a))
#
# print(id(a_instance.b))
# print(id(a_instance.b.a.b))
# print(id(a_instance.b.a.b.a.b))

gc.disable()
print(object_exist(id(a_instance)))

a_instance_id = id(a_instance)
b_instance_id = id(a_instance.b)

a_instance = None

print(ref_count(id(a_instance_id)))
print(ref_count(id(b_instance_id)))

print(object_exist(a_instance_id))
print(object_exist(b_instance_id))

gc.collect()

print(object_exist(a_instance_id))
print(object_exist(b_instance_id))
'''Single-threaded applications'''
from time import perf_counter, sleep


def task():
    print('start')
    sleep(0.1)
    print('end')


start_time = perf_counter()

task()
task()

end_time = perf_counter()

duration = end_time - start_time

print('single thread app running time - {}'.format(duration))

'''multi-threaded program'''
from threading import Thread, Lock


def task(n):
    print('start ' + str(n))
    sleep(0.1)
    print('end' + str(n))


start_time = perf_counter()

threads = []
for i in range(1, 11):
    t = Thread(target=task, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = perf_counter()
duration = end_time - start_time
print('multi thread app running time - {}'.format(duration))

'''Race condition'''

counter = 10


def increase(by, lock):
    global counter

    lock.acquire()

    local_counter = counter
    local_counter += by
    sleep(0.1)
    counter = local_counter
    print('counter={}'.format(counter))
    lock.release()
    sleep(1)


# increase(10)
# increase(20)
# print(counter)

lock = Lock()

thread_1 = Thread(target=increase, args=(10, lock))
thread_2 = Thread(target=increase, args=(20, lock))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print('global counter is {}'.format(counter))
