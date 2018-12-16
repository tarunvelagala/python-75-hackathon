# HANDLING DURATION

from datetime import *
dt = datetime(2018, 12, 20, 13, 2, 10)
duration = timedelta(days=15, hours=10, minutes=30)
print(dt+duration)
print(dt-duration)

# to measure the time taken by the program
from time import *
t1 = perf_counter()
i, sum = 0, 0
while(i < 1000000):
    sum = sum+i
    i += 1

sleep(3)
t2 = perf_counter()

print('execution time= %f seconds' % (t2-t1))
