"""
If given list is [1,2,3,4,5,6,7,8,9,10] => desired output is
[(1,10),(2,9),(3,8),(4,7),(5,6)] 
"""
from collections import deque

print("Enter space separated integer values of list:")
num_list = deque(list(map(int,input().split())))

desired_list = []

num_list_length = len(num_list)

for count in range(num_list_length//2):
    num1, num2 = num_list.popleft(), num_list.pop()
    desired_list.append((num1,num2))

print(desired_list)
