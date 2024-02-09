import math
#1
class Myclass:
    def __init__(self):
        self.string = ""
    def GetString(self):
        self.string = input()
    def PrintString(self):
        self.string = print(self.string.upper())
x = Myclass()
x.GetString()
x.PrintString()

#2
class Shape:
    def area(self) -> None:
        self.a = 0
class Square:
    def __init__(self):
        self.length = int(input())
    def area(self):
        self.a = self.length * self.length
        print(self.a)
x = Square()
x.area()

#3
class Shape:
    def area(self) -> None:
        self.a = 0
class Rectangle:
    def __init__(self,length,width):
        self.length = length 
        self.width = width
    def area(self):
        self.a = self.length * self.width
        print(self.a)
x = Rectangle(int(input()),int(input()))
x.area()

#4
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(f"x:{self.x};y:{self.y}")
    def move(self,newx,newwy):
        self.newx = newx
        self.newwy = newwy
        self.x = self.newx
        self.y = self.newwy
        print(f"Coordinates of x:{self.newx};y:{self.newwy}")
    def dist(self,nx,ny):
        self.nx = nx
        self.ny = ny
        dist = math.sqrt(((self.nx - self.x)**2)+((self.ny - self.y)**2))
        print(f"Distance between 2 points:{dist}")
print("Coordinates of x and y:")
z = Point(int(input()),int(input()))
z.show()
print("New coordinates of x and y:")
z.move(int(input()),int(input()))
print("New point coordinates:")
z.dist(int(input()),int(input()))

#5
class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,dmon):
        self.dmon = dmon
        self.balance += self.dmon
        print(f"Your current balance:{self.balance}")
    def withdraw(self,mon):
        self.mon = mon
        enough = True
        self.balance -= self.mon
        if self.balance < 0:
            enough = False
            self.balance += self.mon
            print("You dont have enough money to withdraw!")
        print(f"Your current balance:{self.balance}")
owner = input("Enter owner name: ")
balance = float(input("Enter initial balance: "))  # Assuming balance can be a float
x = Account(owner, balance)
sel = True
while sel == True:
    print("If you want to deposit: -> 1\nIf you want to withdraw: -> 2\nIf you want to exit: -> 3")
    lo = int(input())
    if lo == 1:
        print("How much money do you want to deposit?")
        x.deposit(int(input()))
    elif lo == 2:
        print("How much money do you want to withdraw?")
        x.withdraw(int(input()))
    elif lo == 3:
        sel = False
    else:
        print("please chose 1 , 2 or 3")
        sel = True

#6
numbers = []
nums = list(map(int,input().split()))
numbers.extend(nums)
prime_nums = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)) and x > 1, numbers))
print("Prime numbers in the list:", prime_nums)