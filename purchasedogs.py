# List to store purchased dogs
purchased_dogs = []

# List of available dogs and their price ranges
dog_breeds = {
    "Labrador": (500, 1500),
    "Bulldog": (600, 2000),
    "Beagle": (300, 1200),
    "Poodle": (800, 2500),
    "Golden Retriever": (700, 1800)
}

# Allowed colors and age range for purchasing
dog_colors = ["Black", "White", "Brown", "Golden", "Gray"]
age_limit = (0, 15)  # Age range in years

# Function to display available dog breeds and price ranges
def display_available_dogs():
    print("\nAvailable Dog Breeds and Price Ranges:")
    for breed, price_range in dog_breeds.items():
        print(f"{breed}: ${price_range[0]} - ${price_range[1]}")

# Function to add a purchased dog with validation
def purchase_dog(name, age, color, breed):
    if breed not in dog_breeds:
        print(f"Error: {breed} is not an available breed.")
        return

    if color not in dog_colors:
        print(f"Error: {color} is not an acceptable color. Choose from {', '.join(dog_colors)}.")
        return

    if not (age_limit[0] <= age <= age_limit[1]):
        print(f"Error: Age must be between {age_limit[0]} and {age_limit[1]} years.")
        return

    purchased_dogs.append({"Name": name, "Age": age, "Color": color, "Breed": breed})
    print(f"Success: {name} the {breed} has been added to your purchases!")

# Function to display dog details
def display_dogs():
    if purchased_dogs:
        print("\nYou have purchased the following dogs:")
        for count, dog in enumerate(purchased_dogs, start=1):
            print(f"{count}. Name: {dog['Name']}, Age: {dog['Age']} years, Color: {dog['Color']}, Breed: {dog['Breed']}")
    else:
        print("\nYou haven't purchased any dogs yet.")

# Example usage
display_available_dogs()

# Display purchased dogs
display_dogs()
