import time

start = time.time()

for i in range(10000):
  i**i

print(time.time() - start)