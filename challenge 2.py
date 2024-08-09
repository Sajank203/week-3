def can_enrol(lives_distance_km, age, right_to_stay, pays_international_fees):
    # Check if the student lives less than 4 km from the school
    if lives_distance_km >= 4:
        return "Student lives too far from the school."
    
    # Check if the student is under 18 years old
    if age < 18:
        # If the student is under 18, they can enroll if they pay international fees
        if pays_international_fees:
            return "Student can enroll (under 18 and paying international fees)."
        else:
            return "Student is under 18 but not paying international fees, so cannot enroll."
    
    # Check if the student has the right to stay in New Zealand
    if not right_to_stay:
        return "Student does not have the right to stay in New Zealand."
    
    # If the student is 18 or older and has the right to stay
    return "Student can enroll."