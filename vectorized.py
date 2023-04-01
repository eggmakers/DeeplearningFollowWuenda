import numpy as np
import time

a = np.random.randn(1000000)
b = np.random.randn(1000000)

tic = time.time()
c = np.dot(a, b)
toc = time.time()

print(c)
print("vectorizd version:" + str(1000 * (toc - tic)) + "ms")

c = 0
tic = time.time()
for i in range(1000000):
    c += a[i] * b[i]
toc = time.time()

print(c)
print("for loop version:" + str(1000 * (toc - tic)) + "ms")