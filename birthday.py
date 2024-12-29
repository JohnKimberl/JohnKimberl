import calendar 
from datetime import datetime

def happy_birthday(name, day):
    return f"Hello how are you {name}! today {day} is the same day as your birthday"

current_day = datetime.now().day  # This gives us current day of month (1-31)
name = input("What is your name?: ")
birthday = int(input("What day of the month were you born on (1-31)?: "))

# Validate the day is within valid range
if birthday < 1 or birthday > 31:
    print("Please enter a valid day between 1 and 31")
else:
    if birthday == current_day:
        x, y = name, birthday  # Fixed variable name from birth_day to birthday
        print(happy_birthday(x, y))
    else:
        # Calculate days until birthday
        if birthday > current_day:
            days_until = birthday - current_day
        else:
            # If birthday has passed, calculate days until next year
            days_until = (31 - current_day) + birthday
            
        print(f"The same date as your the same date as your birthday for this month will be in {days_until} days")
        
     



