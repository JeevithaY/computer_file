# class A:
#
#     def __init__(self, a):
#         self.a = a
#
#     def __add__(self, other):
#         return self.a + other.a
#
#     def __sub__(self, other):
#         return self.a - other.a
#
#     def __mul__(self, other):
#         return self.a * other.a
#
#     def __gt__(self, other):
#         if self.a > other.a:
#             return True
#         else:
#             return False
#
#     def __lt__(self, other):
#         if self.a < other.a:
#             return True
#         else:
#             return False
#
#     def __eq__(self, other):
#         if self.a == other.a:
#             return True
#         else:
#             return False
#
#
# a1 = A(2)
# a2 = A(5)
# print(a1+a2)
# a3 = A("err")
# a4 = A("hai")
# print(a4+a3)
# print(a1-a2)
# print(a1*a2)
# print(a4 > a3)
# print(a1 < a2)
# print(a1 == a2)


class Point:

    def __int__(self, a):
        self.a = a

    @property
    def jeevi(self):
        return self.a

    @jeevi.setter
    def jeevi(self, b):
        self.a = b

    @jeevi.deleter
    def jeevi(self):
        del self.a

obj = Point(3)
print(obj.jeevi)
