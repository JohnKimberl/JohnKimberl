# List to store purchased dogs
purchased_dogs = []

# List of available dogs and their price ranges
dog_breeds = {
    "Labrador": (500, 800, 1500),
    "Bulldog": (600, 1200, 2000),
    "Beagle": (300,500, 800, 1200),
    "Poodle": (800,1000, 1500, 2000 2500),
    "Golden Retriever": (700, 1800),
}

# Allowed colors and age range for purchasing
dog_colors = ["Black", "White", "Brown", "Golden", "Gray"]
age_limit = (0, 15)  # Age range in years

# List of online stores and their price ranges per breed
dog_stores = [
    {"name": "Pet Store A", "prices": {"Labrador": 1200, "Bulldog": 1800, "Beagle": 800, "Poodle": 2000, "Golden Retriever": 1600}},
    {"name": "Dog Haven", "prices": {"Labrador": 1000, "Bulldog": 1500, "Beagle": 600, "Poodle": 2200, "Golden Retriever": 1400}},
    {"name": "Canine World", "prices": {"Labrador": 1300, "Bulldog": 1700, "Beagle": 700, "Poodle": 2400, "Golden Retriever": 1500}},
]

# Function to display available dog breeds and price ranges
def display_available_dogs():
    print("\nAvailable Dog Breeds and Price Ranges:")
    for breed, price_range in dog_breeds.items():
        print(f"{breed}: ${price_range[0]} - ${price_range[2]}")

# Function to display online stores and prices for a specific breed
def display_store_prices(breed):
    print(f"\nPrices for {breed} at various stores:")
    for store in dog_stores:
        if breed in store["prices"]:
            print(f"{store['name']}: ${store['prices'][breed]}")

# Function to add a purchased dog with validation
def purchase_dog(name, age, color, breed, price):
    if breed not in dog_breeds:
        print(f"Error: {breed} is not an available breed.")
        return False
    if color not in dog_colors:
        print(f"Error: {color} is not available. Choose from {', '.join(dog_colors)}.")
        return False
    if not (age_limit[0] <= age <= age_limit[1]):
        print(f"Error: Age must be between {age_limit[0]} and {age_limit[1]} years.")
        return False
    if not (dog_breeds[breed][0] <= price <= dog_breeds[breed][1]):
        print(f"Error: Price must be between ${dog_breeds[breed][0]} and ${dog_breeds[breed][1]}.")
        display_store_prices(breed)
        return False

    purchased_dogs.append({"Name": name, "Age": age, "Color": color, "Breed": breed, "Price": price})
    print(f"Success: {name} the {breed} has been added to your purchases at ${price}!")
    return True

# Function to display purchased dogs
def display_dogs():
    if purchased_dogs:
        print("\nYou have purchased the following dogs:")
        for i, dog in enumerate(purchased_dogs, 1):
            print(f"{i}. Name: {dog['Name']}, Age: {dog['Age']} years, Color: {dog['Color']}, Breed: {dog['Breed']}, Price: ${dog['Price']}")
    else:
        print("\nYou haven't purchased any dogs yet.")

# Main menu function
def main_menu():
    while True:
        print("\n=== Dog Purchase System ===")
        print("1. View Available Dogs")
        print("2. Purchase a Dog")
        print("3. View Purchased Dogs")
        print("4. Search Online Stores")
        print("5. Exit")

        # Input validation for menu choice
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice not in range(1, 6):
                print("Invalid input. Please enter a number between 1 and 5.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            display_available_dogs()
        elif choice == 2:
            name = input("Enter dog's name: ").strip()
            if not name:
                print("Error: Name cannot be empty.")
                continue

            try:
                age = int(input("Enter dog's age (0-15): "))
            except ValueError:
                print(f"Error: Age must be a number between {age_limit[0]} and {age_limit[1]}.")
                continue

            print("\nAvailable colors:", ", ".join(dog_colors))
            color = input("Enter dog's color: ").strip().title()

            print("\nAvailable breeds:", ", ".join(dog_breeds.keys()))
            breed = input("Enter dog breed: ").strip()

            try:
                price = int(input(f"Enter the price for the {breed}: "))
            except ValueError:
                print("Error: Price must be a valid number.")
                continue

            purchase_dog(name, age, color, breed, price)
        elif choice == 3:
            display_dogs()
        elif choice == 4:
            print("\nAvailable breeds to search prices for:", ", ".join(dog_breeds.keys()))
            breed = input("Enter breed to search prices: ").strip()
            if breed in dog_breeds:
                display_store_prices(breed)
            else:
                print(f"Error: {breed} is not an available breed.")
        elif choice == 5:
            print("Thank you for using the Dog Purchase System!")
            break

# Initial program entry point
userchoice = input("Would you like to buy dogs? (y/n): ").lower()
if userchoice in ['y', 'yes']:
    main_menu()
else:
    print("You have successfully exited the program.")
