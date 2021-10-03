
lists =  [ 2, 3]

lists.append([10])


lists.extend([20, 50, 100]) # extend các element

lists  = lists + [150] 
print(lists)

#print(lists * 3)

lists[6:6] = [250, 300, 400] #insert vao vt 6 và đẩ vt 6 sang trái

print(lists)


del lists[1:3]

print(lists)

# del là xoá luôn , clear là chỉ clear item
# del lists xoá luôn list, trở về chưa defined


my_list = ['p','r','o','b','l','e','m']
my_list[2:3] = []

#output my_list: ['p', 'r', 'b', 'l', 'e', 'm']

my_list[2:5] = [] 
#output my_list: ['p', 'r', 'm']


pow2 = [2 ** x for x in range(10)] # 2**x chạy sau cùng
print(pow2) #[1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

pow2 = [2 ** x for x in range(10) if x > 5] # [64, 128, 256, 512]

odd = [x for x in range(20) if x % 2 == 1] #for chạy trước, sau đó chạy if , if đủ đk thì chạy x
#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


[x+y for x in ['Python ','C '] for y in ['Language','Programming']] # for lồng
#['Python Language', 'Python Programming', 'C Language', 'C Programming']


#TUPLE


my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
a, b, c = my_tuple

print(a)      # 3
print(b)      # 4.6
print(c)      # dog


my_tuple = ("hello")
print(type(my_tuple))  # <class 'str'>

# Creating a tuple having one element
my_tuple = ("hello",)
print(type(my_tuple))  # <class 'tuple'>

# Parentheses is optional
my_tuple = "hello",
print(type(my_tuple))  # <class 'tuple'>

#tuple ko thể thay đổi giá trị ở 1 vị trí, tuy nhiên có thể thay đổi giá trị của 1 mảng nằm trong tuple,
# nó có thể thêm giá trị mới vào sau, giống như list chỉ khác mỗi ko thể thay đổi giá trị tại 1 vị trí, trừ giá trị nằm trong mảng
# tuple ko thể  xoá giá trị ở 1 vị trí , chỉ có thể xoá luôn chính nó
my_tuple = (4, 2, 3, [6, 5])
my_tuple[3][0] = 9    

print(my_tuple)

# vì các bộ giá trị là bất biến , nên việc loop sẽ nhanh hơn so với danh sách , hiệu suất tăng nhẹ
# có thể sử dụng làm key cho dict, list thì ko thể.


#STRING

str = 'cold'
print(list(enumerate(str)))
#list(enumerate(str) =  [(0, 'c'), (1, 'o'), (2, 'l'), (3, 'd')]

#SET
#set tự sắp xếp tăng dần, ko giống nhau , và ko cho 1 giá trị nào có thể thay đổi bằng cách gán kể cả mảng
# thay đổi giá trị thông qua function của nó

my_set = {1, 5, 3, 4, 3, 2}

print(my_set)

a = set() # type set ,set() value mặc định
a = {} # type dict

my_set.add(10) # add 1 element
my_set.update([2,5,6]) # add multiple  element
my_set.update([11,9,6], {111,69})
print(my_set)

my_set.discard(10) # xoá đi 1 item, nếu có cũng đc ko có cũng đc
my_set.remove(5) # xoá 1 item , bắt buộc phải có


print(my_set.pop())
print(my_set.pop())

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}


print(A.union(B)) #{1, 2, 3, 4, 5, 6, 7, 8} hợp 2 làm 1 các phần tử duy nhất
print(A.intersection(B)) # lấy ra phần tử giống của 2 bên
print(A.difference(B)) # lấy ra item của A khác bên B
print(A.symmetric_difference(B)) # hợp 2 làm 1 bỏ đi item giống nhau giữa 2 bên


#DICT
# sử dụng my_dict.get("address") thay vì my_dict['address'] vì khi tìm sai tên my_dict.get("address") sẽ trả null còn my_dict['address']  throw lỗi