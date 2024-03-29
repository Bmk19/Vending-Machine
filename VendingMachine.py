# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 08:29:20 2019

@author: Michael Norton
"""

#Firstly, define the items that are inside the vending machines.
class Item: 
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    #Update the available.
    def updateStock(self, stock):
        self.stock = stock

    def stockPurchase(self):
        if self.stock == 0:
            # raise "not item" exception
            pass
        #Reduce the count of stock once it has been purchased.
        self.stock -= 1

# Create the script of the vending machine, and what it will print out.
# This is for the user's interaction with the vending machine.
class VendingMachine:
    def __init__(self):
        self.amount = 0
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def showItems(self):
        print('\nitems available \n***************')

        for item in self.items: #Only show the items in stock.
            if item.stock == 0:
                self.items.remove(item)
        for item in self.items:
            print(item.name, item.price)

        print('***************\n')

    def addCash(self, money):
        self.amount = self.amount + money

    def buyItem(self, item):
        if self.amount < item.price:
            print("You can't but this item. Insert more coins.")
        
        #Return the amount entered, less the price.
        else:
            self.amount -= item.price
            item.stockPurchase()
            print('You got ' + item.name)
            print('Change returned: ' + str(self.amount))

    def containsItem(self, wanted):
        ret = False
        for item in self.items:
            if item.name == wanted:
                ret = True
                break
        return ret

    def getItem(self, wanted):
        ret = None
        for item in self.items:
            if item.name == wanted:
                ret = item
                break
        return ret
    
    #Create a function for the amount of money the customer inserted.
    def insertAmountForItem(self, item):
        price = item.price
        while self.amount < price:
            self.amount = self.amount + float(input('insert ' + str(price - self.amount) + ': '))

    def checkRefund(self):
        if self.amount > 0:
            print(self.amount + " refunded.")
            self.amount = 0

        print('Thank you, have a nice day!\n')


def vending():
    machine = VendingMachine()
    item1 = Item('Bar One', 8.00, 2) #Item name, price, stock.
    item2 = Item('Soft Drink', 12.50, 1)
    item3 = Item('Simba Chips', 6.50, 3)
    item4 = Item('Stimrol', 10.50, 1)
    item5 = Item('Cookies', 13.50, 3)
    machine.addItem(item1) #Add the items to the machine list.
    machine.addItem(item2)
    machine.addItem(item3)
    machine.addItem(item4)
    machine.addItem(item5)

    print('Welcome to the vending machine!\n***************')
   
    #Create an option for a customer to buy for more than one product.
    #This takes place after paying for the previous item.
    continueToBuy = True
    while continueToBuy == True:
        machine.showItems()
        selected = input('select item: ')
        if machine.containsItem(selected):
            item = machine.getItem(selected)

            machine.insertAmountForItem(item)
            machine.buyItem(item)

            a = input('buy something else? (y/n): ')
            if a == 'n':
                continueToBuy = False
                machine.checkRefund()
            else:
                continue

        else:
            print('Item not available. Select another item.')

        continue


vending()
