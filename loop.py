# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

sum  = 0 

for val in numbers:
    sum += val

print("Giá trị là : ", sum)

print(list(range(0, 9)))

numbers.sort(reverse = True)

print(numbers)

print("while loop")

index = 0
while index <= len(numbers) - 1:
    print(f"Giá trị tại index {index} là : {numbers[index]}")
    index+=1


# program to display student's marks from record
student_name = 'James'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(f"Điểm là : {marks[student]}")
        break    
else:
    print('Không tìm thấy.')



counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
    if counter == 3:
        break
else:
    print("Inside else")

numbers = [6, 5, 3,]

for valL in numbers:
    for val in numbers:
        if val == 6:
            continue
        print(f"Giá tri tại {valL} và {val}")


sequence = ['p', 'a', 's', 's']
for val in sequence:
    pass
    print(f"Giá tri tại {val}")

n = 3

for item in range(0, n):
    print(item * item)


def addGa(a, b):
    return a +b