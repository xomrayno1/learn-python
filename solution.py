"""  
# tìm max lớn 2

n = int(input())
arr = map(int, input().split())

newArr = list(arr)

maxFirst = max(newArr)

while maxFirst in newArr:
    newArr.remove(maxFirst)

print(max(newArr))

"""


"""
# tìm min nhất thứ 2 


listsValue = {}

for _ in range(int(input())):
    name = input()
    score = float(input())
    listsValue[name] = score
 
values = listsValue.values() #type dict_values chỉ lấy giá trị [20.0,19.0,...]

print(values)

second = sorted(list(set(values)))[1]

second_list = []

#listsValue.items() chuyển sang view set, [(key,value), (key,value)]

for key,value in listsValue.items():
    if value == second:
        second_list.append(key)

second_list.sort()

for item in second_list:
    print(item)

"""


"""
from functools import reduce
from decimal import Decimal


n = int(input())
student_marks = {}
for _ in range(n):
    line = input().split(" ")
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name] = scores
query_name = input()


for key, values in student_marks.items():
    if key == query_name:
        values = list(values)
        total = reduce(lambda a,b: a + b ,values)
        print("{0:.2f}".format(total / len(values)))
"""


"""
N = int(input())
data = []
for i in range(N):
    line = input().split(" ")
    if line[0] == 'insert':
        data.insert(int(line[1]), int(line[2]))
    elif line[0] == 'print':
        print(data)
    elif line[0] == 'remove':
        data.remove(int(line[1]))
    elif line[0] == 'append':
        data.append(int(line[1]))
    elif line[0] == 'sort':
        data.sort()
    elif line[0] == 'pop':
        data.pop()
    elif line[0] == 'reverse':
        data.reverse()
"""

def print_full_name():
    print(f"Hello {input()} {input()}! You just delved into python.")

if __name__ == '__main__':
    print_full_name()