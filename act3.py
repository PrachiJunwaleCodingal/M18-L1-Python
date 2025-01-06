#Customize your ride
print("Select your ride: ")
print("1. Ola Service")
print("2. Uber Service")

ch = int( input("Enter your choice: ") )

if( ch == 1 ): 
  print( "Do you want a bike or car on rent of Ola Service? " )
  print("1.Bike")
  print("2.Car")


  ch2=int(input("Enter you choice2: "))
  if ch2==1: 
    print("you have selected to rent a bike")
  else:
    print("you have selected to rent a car")


elif( ch == 2 ): 
  print( "Do you want a bike or car on rent of Uber Service? " )
  print("1.Bike")
  print("2.Car")


  ch2=int(input("Enter you choice2: "))
  if ch2==1: 
    print("you have selected to rent a bike")
  else:
    print("you have selected to rent a car")


else:
  print("Wrong choice!")
