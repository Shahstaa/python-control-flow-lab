#Exercise 1:
def check_letter():
    letter = input("Enter a letter: ").lower()  
    if letter.isalpha() and len(letter) == 1:  
        if letter in 'aeiou':  
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid input. Please enter a single letter.")
        
# Call the function
check_letter()
#----------------------------------------------------------------
#Exercise 2:
def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            print("Age cannot be negative.")
        elif age >= 18:
            print("You are eligible to vote!")
        else:
            print("You are not eligible to vote yet.")
    except ValueError:
        print("Invalid input. Please enter a valid number for your age.")
        
# Call the function
check_voting_eligibility()
#----------------------------------------------------------------
#Exercise 3: 
def calculate_dog_years():
    try:
        dog_age = int(input("Input a dog's age: "))
        if dog_age <= 2:
            dog_years = dog_age * 10  
        else:
            dog_years = 20 + (dog_age - 2) * 7  
        print(f"The dog's age in dog years is {dog_years}.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the dog's age.")
        
# Call the function
calculate_dog_years()
#----------------------------------------------------------------
#Exercise 4: 
def weather_advice():
    is_cold = input("Is it cold? (yes/no): ").lower() == "yes"
    is_raining = input("Is it raining? (yes/no): ").lower() == "yes"
    
    if is_cold and is_raining:
        print("Wear a waterproof coat.")
    elif is_cold and not is_raining:
        print("Wear a warm coat.")
    elif not is_cold and is_raining:
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")
        
# Call the function
weather_advice()
#----------------------------------------------------------------
#Exercise 5:
def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").capitalize()
    try:
        day = int(input("Enter the day of the month: "))
        if month in ['Dec', 'Jan', 'Feb'] or (month == 'Mar' and day <= 19):
            season = "Winter"
        elif month in ['Mar', 'Apr', 'May'] or (month == 'Jun' and day <= 20):
            season = "Spring"
        elif month in ['Jun', 'Jul', 'Aug'] or (month == 'Sep' and day <= 21):
            season = "Summer"
        elif month in ['Sep', 'Oct', 'Nov'] or (month == 'Dec' and day <= 20):
            season = "Fall"
        else:
            print("Invalid date.")
            return
        print(f"{month} {day} is in {season}.")
    except ValueError:
        print("Invalid input. Please enter a valid day of the month.")
        
# Call the function
determine_season()