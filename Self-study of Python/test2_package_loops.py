print("Enter your name")
name = input()
print("Enter the accurate weight of the packege")
weight = float(input())
destination = ["Local", "National", "International"]
print("Choose the destination:")
for i, item in enumerate(destination):
    print(f"{i + 1}. {item}")
while True:
    try:
        chosen_destination = int(input()) -1
        if 0 <= chosen_destination < len(destination):
            chosen_destination = destination[chosen_destination]
            if chosen_destination == "Local":
                local_price = weight * 5
                print(f"Dear {name}, your package weights {weight}KG and it's destination is {chosen_destination}.")
                print(f"The cost of the shipment will be {local_price}.")
                if weight > 20:
                    print("⚠ Heavy package warning!")
                break
            elif chosen_destination == "National":
                national_price = weight * 10
                print(f"Dear {name}, your package weights {weight}KG and it's destination is {chosen_destination}.")
                print(f"The cost of the shipment will be {national_price}.")
                if weight > 20:
                    print("⚠ Heavy package warning!")
                break
            elif chosen_destination == "International":
                international_price = weight * 20
                print(f"Dear {name}, your package weights {weight}KG and it's destination is {chosen_destination}.")
                print(f"The cost of the shipment will be {international_price}.")
                if weight > 20:
                    print("⚠ Heavy package warning!")
                break
        else:
            print(f"Invalid choice. Try again.")
            for i, item in enumerate(destination):
                print(f"{i + 1}. {item}")
    except ValueError:
        print("Please enter a valid number.")
        for i, item in enumerate(destination):
            print(f"{i + 1}. {item}")