# -*- coding: utf-8 -*-
"""PythonBudget.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uA28NKX0bVD8rO6LAa27Jqb0N4f8fWsB
"""

class Budget:
    def __init__ (self,name,amount,rent,lights,car,phone,discretionary,needs,laundry):
        self.name = name
        self.amount = amount
        self.rent = rent
        self.lights = lights
        self.car = car
        self.phone = phone
        self.discretionary = discretionary
        self.needs = needs
        self.laundry = laundry
    def monthly_budget(self):
        return f'Hello {self.name}. Ready to Budget?'
    def leftover(self):
        if (self.amount - (self.rent+self.lights+self.car+self.phone+self.discretionary+self.needs+self.laundry)) >= 0:
            print("Hello", self.name, "Your leftover balance for the month is: $", self.amount - (self.rent+self.lights+self.car+self.phone+self.discretionary+self.needs+self.laundry))
        elif (self.amount - (self.rent+self.lights+self.car+self.phone+self.discretionary+self.needs+self.laundry))<0:
            print("So..um..", self.name, 'You are screwed!!!')
print('Hello, are you ready to begin?')
print('')
my_budget = Budget("Hannah",int(input("Your Monthly Amount is: $")),int(input("Your Rent is: $")),int(input("Your Lights are: $")),int(input("Your Car is: $")),int(input("Your Phone is: $")),int(input("Your Discretionary is: $")),int(input("Your Needs Are: $")),int(input("Your Laundry is: $")))
my_budget.leftover()

total = 0
for num in [1, 2, 3, 4]:
    total += num

print(total)