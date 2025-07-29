products = {
    "Gummy Bears": "5₪",
    "Chocolate Bar": "8₪",
    "Lollipop": "3₪",
    "Sour Strips": "6₪"
}

name = input("Enter your name: ")
while True:
    vip = input("Are you a VIP customer? (Yes/No): \n").strip().lower()
    if vip == "yes":
        break
    elif vip == "no":
        break
    else:
        print("Invalid input")
customer = {name : vip}
print(f"\nWelcome {name}!\n")

print("What would you like to buy?")
for i, (key, value) in enumerate(products.items()):
    print(f"{i + 1}. {key} - {value}")
while True:
    item = int(input("\nPlease choose a product: "))
    if item < 1 or item > len(products):
        print("Invalid product number. Please choose a number from the list.")
    else:
        
    quantity = int(input("\n How many? "))
    if quantity < 0:
        print("Invalid quantity.")
        continue
basket = {item : quantity}
