import os
os.system("cls")


##### sonlarni kvadrati va kubini chiqarish dasturi
# def createria(num):
#     def filtering(exponential):
#         return num ** exponential
#     return filtering

# print(createria(10)(2))    
# print(createria(50)(3))    






###### eng uz tillarida salomlashish
# a = "Uz"
# b = "Eng"

# def salomlash(ism):
#     def til(til):
#         return f"Salom {ism}" if til == a else f"Hello {ism}"
#     return til

# print(salomlash("Humoyiddin")("Uz"))







#######  1st question
# x = 0   
# def counter():
#     def count():
#         global x
#         x += 1
#         return x
#     return count
# print(counter()())
# print(counter()())
# print(counter()())







######   2nd question
# def number(num):
#     def numbers(nums):
#         return [i for i in nums if i > num]
#     return numbers

# print(number(10)([12, 34, 54, 45, 1, -4521689, 10, 5, 8, 9]))








#####     3nd question
# def numbers(a, b):
#     def operation(oper):
#         return f"{a} {oper} {b} = {a + b}" if oper == "+" \
#             else f"{a} {oper} {b} = {a - b}" if oper == "-" \
#             else f"{a} {oper} {b} = {a * b}" if oper == "*" \
#             else f"{a} {oper} {b} = {a // b}"
#     return operation

# print(numbers(3, 5)("+"))
# print(numbers(10, 2)("*"))
# print(numbers(20, 5)("/"))
# print(numbers(7, 5)("-"))







######        4th question
# def mezon(createria):
#     def numbers(nums):
#         return [i for i in nums if createria(i)]
#     return numbers

# print("toq sonlar: ", mezon(lambda x: x % 2 == 1)([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print("Juft sonlar: ", mezon(lambda x: x % 2 == 0)([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))








#####          5th questions
# def createria(creater):
#     def numbers(nums):
#         return [num for num in nums if creater(num)]
#     return numbers

# print(createria(lambda x : str(x) == str(x)[::-1]) ([121, 654436, 234, 242, 656, 78, 989, 12]))
# print(createria(lambda x : str(x) == str(x)[::-1]) ([678, 456, 123, 343, 696, 565, 343, 123456654321, 567765]))







####        6th question
# def createriya(creater):
#     def numbers(nums):
#         return [num for num in nums if creater(num)]
#     return numbers

# print("Tub sonlar: ", createriya(lambda x: all(x % i != 0 for i in range(2, x))) ([121, 23, 46, 17, 242, 656, 3, 78, 989, 71, 12]))