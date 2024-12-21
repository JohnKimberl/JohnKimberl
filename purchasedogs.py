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

# Function to display available dog breeds and price ranges
def display_available_dogs():
    print("\nAvailable Dog Breeds and Price Ranges:")
    for breed, price_range in dog_breeds.items():
        print(f"{breed}: ${price_range[0]} - ${price_range[1]}")

# Function to display dog details
def display_dogs():
    if purchased_dogs:
        print("\nYou have purchased the following dogs:")
        count = 1
        for dog in purchased_dogs:
            print(f"{count}. Name: {dog['Name']}, Age: {dog['Age']} years, Color: {dog['Color']}")
            count += 1
    else:
        print("\nYou haven't purchased any dogs yet.")

# Function to add a dog
def add_dog(name, age, color):
    dog = {"Name": name, "Age": age, "Color": color}
    purchased_dogs.append(dog)

# Function to search for the best store to purchase a dog
def find_best_store(breed):
    print(f"\nSearching for the best store to purchase a {breed}...")
    # In a real program, you could use an API or web scraping to find stores.
    print(f"Search results for {breed}:")
    print("- PetWorld: Best prices and free shipping!")
    print("- HappyPaws: Excellent customer reviews!")
    print("- DoggosStore: Wide variety of breeds available!")

# Main program
while True:
    display_available_dogs()
    user_choice = input("\nWould you like to purchase a dog? (Yes/No): ").strip().lower()

    if user_choice == "no":
        print("\nThank you for visiting! Goodbye!")
        break
    elif user_choice == "yes":
        breed_choice = input("Enter the breed of the dog you want to purchase: ").strip().title()

        if breed_choice in dog_breeds:
            print(f"\nThe price range for a {breed_choice} is ${dog_breeds[breed_choice][0]} to ${dog_breeds[breed_choice][1]}.")
            name = input("Enter the dog's name: ").strip()
            age = input("Enter the dog's age (in years): ").strip()
            color = input("Enter the dog's color: ").strip()

            # Add the dog to the list
            add_dog(name, age, color)
            print(f"\nYou've added {name} to your list of purchased dogs!")
            
            # Display all purchased dogs
            display_dogs()

            # Ask if the user wants to find the best store
            search_store = input(f"Would you like to find the best store to purchase a {breed_choice}? (Yes/No): ").strip().lower()
            if search_store == "yes":
                find_best_store(breed_choice)
            else:
                print("\nOkay, enjoy your shopping!")
        else:
            print("\nSorry, we don't have that breed available. Please choose from the listed breeds.")
    else:
        print("\nInvalid input. Please type 'Yes' or 'No'.")
