print("Welcome to 'Best Pizza in da town'!")
      
user_choice = input("Choose your size: S, M or L?\n").upper()
add_pepperoni = input("Would you like to add pepperoni? Y or N?\n").upper()
add_cheese = input("Would you like to add some cheese? Y or N?\n").upper()

price = 15
if user_choice == "S":
  price += 0
elif user_choice == "M" or user_choice == "L":
  price += 10

if add_pepperoni == "Y" and user_choice == "S":
  price += 3
elif add_pepperoni == "Y":
  price += 5

if add_cheese == "Y" and user_choice == "S":
  price += 1
elif add_cheese == "Y":
  price += 2

if add_pepperoni == "Y" and add_cheese == "Y":
  print(f"Your choice is: {user_choice} size, with extra pepperoni and extra cheese.")
elif add_pepperoni == "Y":
  print(f"Your choice is: {user_choice} size, with extra pepperoni.")
elif add_cheese == "Y":
  print(f"Your choice is: {user_choice} size, with extra cheese.")
else:
  print(f"Your choice is: {user_choice} with no extras.")


check = input("Is it correct? Y or N?\n").upper()

if check == "Y":
  print(f"The total price is: {price}.")
else:
  print("Please reorder.")
