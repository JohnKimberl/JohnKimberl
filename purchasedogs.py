# List to store purchased dogs
purchased_dogs = []

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

# Main program
while True:
    user_choice = input("Would you like to purchase a dog? (Yes/No): ").strip().lower()

    if user_choice == "no":
        print("\nThank you for visiting! Goodbye!")
        break
    elif user_choice == "yes":
        name = input("Enter the dog's name: ").strip()
        age = input("Enter the dog's age (in years): ").strip()
        color = input("Enter the dog's color: ").strip()
        
        # Add the dog to the list
        add_dog(name, age, color)
        print(f"\nYou've added {name} to your list of purchased dogs!")
        
        # Display all purchased dogs
        display_dogs()
    else:
        print("\nInvalid input. Please type 'Yes' or 'No'.")

  

