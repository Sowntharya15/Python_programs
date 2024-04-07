from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    def area(self, l, b):
        return l * b

    def perimeter(self, l, b):
        return 2 * (l + b)


class Circle(Shape):
    def area(self,r):
        return (3.14 * r * r)

    def perimeter(self, r):
        return (2 * 3.14 * r)


class Triangle(Shape):
    def area(self, s1, s2, s3):
        a = (s1 + s2 + s3) // 2
        area = (a * (a - s1) * (a - s2) * (a - s3)) ** 0.5
        return area

    def perimeter(self, s1, s2, s3):
        b = (s1 + s2 + s3) // 2
        return b


n = int(input())
if n == 1:
    r1 = Rectangle()
    print("Area:", r1.area(5, 6))
    print("Peri:", r1.perimeter(5, 6))
elif n == 2:
    c1 = Circle()
    print("Area:", c1.area(3))
    print("Peri:", c1.perimeter(3))
elif n == 3:
    t1 = Triangle()
    print("Area:", t1.area(3, 4, 5))
    print("Per:", t1.perimeter(3, 4, 5))
