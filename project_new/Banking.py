# total_amount = 0
# while True:
#     a = input()
#     if a == "":
#         break
#     else:
#         a = a.split(" ")
#         if a[0] == "D":
#             total_amount = total_amount + int(a[1])
#         elif a[0] == "W":
#             total_amount = total_amount - int(a[1])
# print(total_amount)

s = "i love my india india is my country"
from collections import defaultdict
d = defaultdict(int)
for word in s.split():
    d[word] += 1
print(d)