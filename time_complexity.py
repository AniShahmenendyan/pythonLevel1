#!/usr/bin/env python
import matplotlib.pyplot as plt
import time
import numpy
import sys

sys.setrecursionlimit(1000000)

arr_of_arr = []
for i in range(10, 1000):
    arr = numpy.random.randint(100, 10000, i)
    arr_of_arr.append(arr)


def rob_wrapper(lst):
    memo = {}

    def rob(index):
        if index > len(lst) - 1:
            return 0

        if index in memo:
            return memo[index]

        res = max(lst[index] + rob(index + 2), rob(index + 1))
        memo[index] = res
        return res

    return rob(0)


def rob_edgar(arr):
    n = len(arr)

    if n == 0:
        return 0

    if n == 1:
        return arr[0]

    s = [0] * (n + 1)
    s[1] = arr[0]
    s[2] = arr[1]

    for i in range(3, n + 1):
        s[i] = (max(s[i - 2], s[i - 3]) + arr[i - 1])
    return max(s[n], s[n - 1])


# In[5]:


def rob_davit(nums):
    prev2 = 0
    prev1 = 0
    for i in range(0, len(nums)):
        temp = prev1
        prev1 = max(prev2 + nums[i], prev1)
        prev2 = temp

    return prev1


# In[ ]:


times_rob_edgar = []

for i in range(len(arr_of_arr)):
    start = time.perf_counter()
    rob_edgar(arr_of_arr[i])
    end = time.perf_counter()

    times_rob_edgar.append((end - start) * 1000)

# In[ ]:


times_rob_wrapper = []

for i in range(len(arr_of_arr)):
    start = time.perf_counter()
    rob_wrapper(arr_of_arr[i])
    end = time.perf_counter()

    times_rob_wrapper.append((end - start) * 1000)

# In[ ]:


times_rob_davit = []

for i in range(len(arr_of_arr)):
    start = time.perf_counter()
    rob_davit(arr_of_arr[i])
    end = time.perf_counter()

    times_rob_davit.append((end - start) * 1000)

# In[ ]:


plt.plot(times_rob_davit, label='times_rob_davit')
plt.plot(times_rob_edgar, label='times_rob_edgar')
plt.plot(times_rob_wrapper, label='times_rob_wrapper')

plt.legend()
# plt.xlim(0, 10000)
plt.show()
