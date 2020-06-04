from collections import deque
import time

deque_list = deque()
for i in range(10):
    deque_list.append(i)
print(deque_list)

deque_list.appendleft(-1)
print(deque_list)

deque_list.rotate(2)
print(deque_list)
deque_list.rotate(2)
print(deque_list)

print(deque(reversed(deque_list)))

deque_list.extend([5,6,7])
print(deque_list)

deque_list.extendleft([5,6,7])
print(deque_list)

deque_list.clear()

start_time = time.process_time()
for i in range(1000):
    for j in range(10000):
        deque_list.append(j);
        deque_list.pop()
print("queue: ", time.process_time()-start_time," second")

start_time = time.process_time()
just_list=[]
for i in range(1000):
    for j in range(10000):
        just_list.append(j);
        just_list.pop()
print("list: ", time.process_time()-start_time," second")

