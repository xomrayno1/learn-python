class Bird:
    def __init__(self, name):
        self.name = name
    
    def getName(seft):
       return seft.name

class Penguin(Bird): # kế thừa

    def __init__(self, name, color, id):
        super().__init__(name)
        self.color = color
        self.__id__ = id #__id__ tránh truy cập từ bên ngoài , đóng gói
    
    def getInfo(seft):
        print(f"Chim Tên : {seft.name} có màu {seft.color} và có id {seft.__id__}")

    def setId(seft, newId):
        seft.__id__ = newId

    def fly(self):
        print("Penguin can't fly")

class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")

def flying_test(bird): ## miễn là bird, đa hình
    bird.fly()

birdPenguin = Penguin("gà", "red", 1)
birdParrot = Parrot()

birdPenguin.getInfo()
birdPenguin.color = "blue"
birdPenguin.setId(2)
birdPenguin.getInfo()

flying_test(birdParrot)
flying_test(birdPenguin)