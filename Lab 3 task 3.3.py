#task 3.3
numberOfDrinks = int((input("Enter how many drinks:")))
pricePerDrink = float(input("Please enter your dink prices: "))        
totalPrice=(numberOfDrinks * pricePerDrink)
print("£", "%10.2f"%totalPrice)
