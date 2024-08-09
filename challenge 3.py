def get_chinese_zodiac_animal(year):
    # List of animals in the 12-year cycle
    zodiac_animals = [
        "Dragon", "Snake", "Horse", "Sheep", "Monkey", "Rooster", 
        "Dog", "Pig", "Rat", "Ox", "Tiger", "Hare"
    ]
    
    # The base year for reference is 2000 (Dragon year)
    base_year = 2000
    
    # Calculate the index of the animal in the cycle
    index = (year - base_year) % 12
    
    # Return the animal corresponding to the calculated index
    return zodiac_animals[index]