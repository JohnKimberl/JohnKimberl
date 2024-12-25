# List to store purchased dogs
userchoice = input("Would you like to buy dogs? (y/n): ").lower()
if userchoice != "y" or "yes":
    print("You have successfully exited the program.")
    exit()

purchased_dogs = []

# List of available dogs and their price ranges
dog_breeds = {
    "Labrador": (500, 1500),
    "Bulldog": (600, 2000),
    "Beagle": (300, 1200),
    "Poodle": (800, 2500),
    "Golden Retriever": (700, 1800),
}

# Allowed colors and age range for purchasing
dog_colors = ["Black", "White", "Brown", "Golden", "Gray"]
age_limit = (0, 15)  # Age range in years

# List of online stores
dog_stores = [
    {"name": "Pet Store A", "url": "https://www.petstorea.com"},
    {"name": "Dog Haven", "url": "https://www.doghaven.com"},
    {"name": "Canine World", "url": "https://www.canineworld.com"},
]

# Function to display available dog breeds and price ranges
def display_available_dogs():
    print("\nAvailable Dog Breeds and Price Ranges:")
    for breed, price_range in dog_breeds.items():
        print(f"{breed}: ${price_range[0]} - ${price_range[1]}")

# Function to display online stores
def display_online_stores():
    print("\nOnline Stores to Purchase Dogs:")
    for store in dog_stores:
        print(f"{store['name']}: {store['url']}")

# Function to add a purchased dog with validation
def purchase_dog(name, age, color, breed):
    if breed not in dog_breeds:
        print(f"Error: {breed} is not an available breed.")
        return

    if color not in dog_colors:
        print(f"Error: {color} is not available. Choose from {', '.join(dog_colors)}.")
        return

    if not (age_limit[0] <= age <= age_limit[1]):
        print(f"Error: Age must be between {age_limit[0]} and {age_limit[1]} years.")
        return

    purchased_dogs.append({"Name": name, "Age": age, "Color": color, "Breed": breed})
    print(f"Success: {name} the {breed} has been added to your purchases!")

# Function to display purchased dogs
def display_dogs():
    if purchased_dogs:
        print("\nYou have purchased the following dogs:")
        i = 1
        for dog in purchased_dogs:
        print(f"{i}. Name: {dog['Name']}, Age: {dog['Age']} years, Color: {dog['Color']}, Breed: {dog['Breed']}")
        i += 1
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
        choice = input("Enter your choice (1-5): ")
        if not choice.isdigit() or int(choice) not in range(1, 6):
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        choice = int(choice)
        if choice == 1:
            display_available_dogs()
        elif choice == 2:
            name = input("Enter dog's name: ")
            age = input("Enter dog's age (0-15): ")
            if not age.isdigit() or not (age_limit[0] <= int(age) <= age_limit[1]):
                print(f"Error: Age must be a number between {age_limit[0]} and {age_limit[1]}.")
                continue
            age = int(age)
            print("\nAvailable colors:", ", ".join(dog_colors))
            color = input("Enter dog's color: ")
            print("\nAvailable breeds:", ", ".join(dog_breeds.keys()))
            breed = input("Enter dog breed: ")
            purchase_dog(name, age, color, breed)
        elif choice == 3:
            display_dogs()
        elif choice == 4:
            display_online_stores()
        elif choice == 5:
            print("Thank you for using the Dog Purchase System!")
            break

main_menu()
