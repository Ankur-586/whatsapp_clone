# s = "abcdefghijklmnopqrstuvwxyz007"
# # Exp_ output: s = "0346bfghjkmoquvwxz"
# number = ['0','1','2','3','4','5','6','7','8','9']
# Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# comb = number + Alphabet
# fl = []
# for i in s:
#     fl.append(i)
# not_pre = []
# for a in comb:
#     if a not in fl:
#         not_pre.append(a)
# x = ''.join(not_pre)
# print(x)

# s = "45ANKUR"
# s1 = s[::-1]
# #EX o/p: 45ANKSAR
# lenght = len(s1)
# s1 = s.replace('4','9')
# print(s1)

item_cart = []
class item():
    def __init__(self,name: str, price: int):
        self.item_name = name
        self.item_price = price
    def show_item(self):
        self.n
class ShoppingCart():
    def add(self):
        Name = input("Enter Item Name: ")
        Price = int(input("Enter Price: "))
        item1 = item(Name,Price)
        print(item1)
s1 = ShoppingCart()
s1.add()
