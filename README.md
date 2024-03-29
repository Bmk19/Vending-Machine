# Vending Machine

Right now, the code may run in the console. A GUI can be added in the future.\
In this exercise you will build the brains of a vending machine. It will accept money, return change, track inventory levels, and dispense products. All the things that you might expect a vending machine to accomplish.


## Features


### Accept Coins

As a vendor
I want a vending machine that accepts coins
So that I can collect money from the customer

The vending machine will accept valid coins and notes (R100, R20, R10 notes; R5, R2, R1, 50c, 20c, 10c coins). When a valid coin is inserted the amount of the coin will be added to the current amount and the display will be updated. When there are no coins inserted, the machine displays INSERT COIN. Rejected coins are placed in the coin return.

### Select Product

As a vendor
I want customers to select products
So that I can give them an incentive to put money in the machine

There are five products: Bar one for R8.00, Soft Drink for R12.50, Simba Chips for R6.50, Stimrol gum for R10.50, a roll of cookies for R13.50.
When the respective item is typed in for order, and enough money has been inserted, the product is dispensed and the machine displays:\ 
You got [item]\
Change returned: [x.xx]\
buy something else? (y/n): 

If the display is checked again, it will display SELECT ITEM and the current amount will be set to $0.00. If there is not enough money inserted then the machine displays PRICE and the price of the item and subsequent checks of the display will display either INSERT COIN or the current amount as appropriate.

### Make Change

As a vendor
I want customers to receive correct change
So that they will use the vending machine again

When a product is selected that costs less than the amount of money in the machine, then the remaining amount is placed in the coin return.

### Return Coins

As a customer
I want to have my money returned
So that I can change my mind about buying stuff from the vending machine

When the return coins button is pressed, the money the customer has placed in the machine is returned and the display shows INSERT COIN.

### Sold Out

As a customer
I want to be told when the item I have selected is not available
So that I can select another item

When the item selected by the customer is out of stock, the machine displays SOLD OUT. If the display is checked again, it will display the amount of money remaining in the machine or INSERT COIN if there is no money in the machine.

### Exact Change Only

As a customer
I want to be told when exact change is required
So that I can determine if I can buy something with the money I have before inserting it

When the machine is not able to make change with the money in the machine for any of the items that it sells, it will display EXACT CHANGE ONLY instead of INSERT COIN.
