""" \
'Create a real time scenario for inheritance example Banking concept, ecommerce concept.' \
"""
# Single Inheritance
class Bank:
    def Sbank(self):
        print("This is SBI bank ")
class Branch(Bank):
    def Bbank(Bank):
        print("This is SBI Hingna Branch ")
bk = Branch()
bk.Sbank()
bk.Bbank()

# Multiple Inheritance
class Account:
    def Cname(self):
        print("Enter Your Name : ")
class Acnum:
    def Acnu(self):
        print("Your Account No  : ")
class Details(Account, Acnum):
    def Bbank(self):
        print("Your Account type  : ")
bo = Details()
bo.Cname()
bo.Acnu()
bo.Bbank()
# Hierarchical Inheritance
class RBI:
    def Bank(self):
        print("This is The RBI Bank ")
class SBI(RBI):
    def subbank(self):
        print("SBI Came under RBI")
class ICICI(RBI):
    def subbank2(self):
        print("ICICI Came under RBI")

op = SBI()
op1 = ICICI()
op.Bank()
op.subbank()
print("----------------------------------------------------------------------")
class Bank_Account:
    def __init__(self):
        self.balance = 0
        print('Welcome to The Deposit & Withdrawal Machine')
    def deposit(self):
        amount = float(input('Enter amount to be Deposited : '))
        self.balance += amount
        print("\n Amount Deposited : ",amount)
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn : "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew : ", amount)
        else:
            print("\n Insufficient Balance ")
class  Display(Bank_Account):
    def display(self):
        print("\n Net Available Balance : ",self.balance)
s = Display()
s.deposit()
s.withdraw()
s.display()

print("----------------------------------------------------------------------")
class Bank_Account:
    def __init__(self):
        self.balance = 0
        print('Welcome to The Deposit & Withdrawal Machine')
class Money:
    def deposit(self):
        amount = float(input('Enter amount to be Deposited : '))
        self.balance += amount
        print("\n Amount Deposited : ",amount)
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn : "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew : ", amount)
        else:
            print("\n Insufficient Balance ")
class  Display(Bank_Account,Money):
    def display(self):
        print("\n Net Available Balance : ",self.balance)
ob = Display()
ob.deposit()
ob.withdraw()
ob.display()
print("----------------------------------------------------------------------")
# syntax_of_single_inheritance


class Brands:  # parent_class
    brand_name_1 = "Amazon"
    brand_name_2 = "Ebay"
    brand_name_3 = "OLX"


class Products(Brands):  # child_class
    prod_1 = "Online Ecommerce Store"
    prod_2 = "Online Store"
    prod_3 = "Online Buy Sell Store"


obj_1 = Products()  # Object_creation
print(obj_1.brand_name_1 + " is an " + obj_1.prod_1)
print(obj_1.brand_name_2 + " is an " + obj_1.prod_2)
print(obj_1.brand_name_3 + " is an " + obj_1.prod_3)
print("----------------------------------------------------------------------")
# example_of_multiple_inheritance

class Brands:               #parent_class
    brand_name_1 = "Amazon"
    brand_name_2 = "Ebay"
    brand_name_3 = "OLX"

class Products:            #child_class
    prod_1 = "Online Ecommerce Store"
    prod_2 = "Online Store"
    prod_3 = "Online Buy Sell Store"
class Popularity(Brands,Products):
     prod_1_popularity = 100
     prod_2_popularity = 70
     prod_3_popularity = 60

obj_1 = Popularity()          #Object_creation#
print(obj_1.brand_name_1+" is an "+obj_1.prod_1+" popularity of "+str(obj_1.prod_1_popularity))
print(obj_1.brand_name_2+" is an "+obj_1.prod_2+" popularity of "+str(obj_1.prod_2_popularity))
print(obj_1.brand_name_3+" is an "+obj_1.prod_3+" popularity of "+str(obj_1.prod_3_popularity))
print("----------------------------------------------------------------------")
# multilevel
class Brands:  # parent_class
  brand_name_1 = "Amazon"
  brand_name_2 = "Ebay"
  brand_name_3 = "OLX"


class Products(Brands):  # child_class
    prod_1 = "Online Ecommerce Store"
    prod_2 = "Online Store"
    prod_3 = "Online Buy Sell Store"


class Popularity(Products):  # grand_child_class
    prod_1_popularity = 100
    prod_2_popularity = 70
    prod_3_popularity = 60


obj_1 = Popularity()  # Object_creation
print(obj_1.brand_name_1 + " is an " + obj_1.prod_1 + " popularity of " + str(obj_1.prod_1_popularity))
print(obj_1.brand_name_2 + " is an " + obj_1.prod_2 + " popularity of " + str(obj_1.prod_2_popularity))
print(obj_1.brand_name_3 + " is an " + obj_1.prod_3 + " popularity of " + str(obj_1.prod_3_popularity))
print("----------------------------------------------------------------------")


# example_of_multilevel_inheritance

class Brands:  # parent_class
    brand_name_1 = "Amazon"
    brand_name_2 = "Ebay"
    brand_name_3 = "OLX"


class Products(Brands):  # child_class
    prod_1 = "Online Ecommerce Store"
    prod_2 = "Online Store"
    prod_3 = "Online Buy Sell Store"


class Popularity(Brands):  # grand_child_class
    prod_1_popularity = 100
    prod_2_popularity = 70
    prod_3_popularity = 60


class Value(Brands):
    prod_1_value = "Excellent Value"
    prod_2_value = "Better Value"
    prod_3_value = "Good Value"


obj_1 = Products()  # Object_creation
obj_2 = Popularity()
obj_3 = Value()
print(obj_1.brand_name_1 + " is an " + obj_1.prod_1 + " popularity of " + str(
    obj_2.prod_1_popularity) + " having " + obj_3.prod_1_value)
print(obj_1.brand_name_1 + " is an " + obj_1.prod_1 + " popularity of " + str(
    obj_2.prod_2_popularity) + " having " + obj_3.prod_2_value)
print(obj_1.brand_name_1 + " is an " + obj_1.prod_1 + " popularity of " + str(
    obj_2.prod_3_popularity) + " having " + obj_3.prod_3_value)
print("----------------------------------------------------------------------")
