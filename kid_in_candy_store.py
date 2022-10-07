# The list of candies to print to the screen
candy_list = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish", "Skittles", "Hershey Bar", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candy_cart = []

# Print out options
for candy in candy_list:
    print(f"[{str(candy_list.index(candy))}] {candy}")
print("which candy do you want?")
for x in range(allowance):
    selected = input("input number of candy you want:  ")
    candy_cart.append(candy_list)[int(selected)])
    print("I brough home with me...")
for candy in candy_cart:
    print(candy)

