import loop as l


x = 10 
def sum(a, b):
    global x
    x = 20
    print(f"X = {x}")
    return a + b

print(sum( a = 10, b = 15))


print(f"X = {x}")


def foo():
    x = 20

    def bar():
        global x
        x = 25
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main: ", x)


def greets(*names):
    """This function greets all
    the person in the names tuple."""      
    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


greets("Monica", "Luke", "Steve", "John")

#filter

lists = [1,2,3,5,7,10]

nums = list(filter(lambda item: item % 2 == 0 ,lists))

print(nums)

#map

nums = list(map(lambda item: item * 2 ,lists))

print(nums)


print(l.addGa(3, 105))

print(["re"] * 3)
