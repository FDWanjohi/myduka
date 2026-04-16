class Person:
    def __init__(self,name,age,address,email):
        self.name = name
        self.age = age
        self.address = address
        self.email = email

    def talks(self):
        print(f"{self.name} talks")

    def walks(self):
        print(f"{self.name} is walking")

        

#person1 object
person1 = Person("Mike",24,'Karen','mike@nail.com')
print (type(person1))
print(person1.address)
person1.talks()
person1.walks()

#person2 object
person2 = Person("Kate",21,'Eastleigh','kate@mail.com')
print(type(person2))
print(person2.address)
person2.talks()
person2.walks()


#1. Create a class calls BankAccount with the following attributes: -account number - balance -owner name -date opened
#2. Give the above BankAccount class the following behavior or methods: -deposit() -withdraw() -display_info()
#3. Create two BankAccount objects that can deposit, withdraw and display_info

class BankAccount:
    def __init__(self, account_number, balance, owner_name, date_opened):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened

        def deposit(self):
            print(f"{self.account_number} deposit")

        def withdraw(self):
            print(f"{self.account_number} withdraw")

        def display_info(self):
            print(f"{self.account_number} display_info")


BankAccount1 = BankAccount(11234567,1234567,"Ell Ell","May_31_2020")
print(type(BankAccount1))
print(f"{self.BankAccount1} can deposit")
print(f"{self.BankAccount1} can withdraw")
print(f"{self.BankAccount1} can display_info")

BankAccount2 = BankAccount(22234567,2234567,"Toria Toria","Jul_31_2020")
print(type(BankAccount2))
print(f"{self.BankAccount2} can deposit")
print(f"{self.BankAccount2} can withdraw")
print(f"{self.BankAccount2} can display_info")

#Create a Car Class Have the following attributes brand - model - year -fuel_capacity - fuel_level -is_running(boolen value) 
# Have the following methods as behaviour for your class: start() stop() refuel() drive() display_car_info()

class car:
    def __init__(self, model, year, fuel_capacity, fuel_level, is_running):
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_level
        self.is_running = is_running
    
      def talks(self):
        print(f"{self.name} talks")

    def start(self):
        print(f"{self.model} starts")

    def stop(self):
        print(f"(self.model) stops")

    def refuel(self):
        print(f"{self.model} refuels")

    def drive(self):
        print(f"{self.model} drives")

    def display_car_info(self):
        print(f"{self.model}" display_car_info)







        
