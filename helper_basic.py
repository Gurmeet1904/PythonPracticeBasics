def days_to_units(num_of_days, conversion_unit):
    if conversion_unit  == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    elif conversion_unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} seconds"
    else:
        return "unsupported unit \n"

def validate_and_execute(days_and_unit_dictionary):
    # if user_input.isdigit():
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0!! Please enter a valid positive number! \n")
        else:
            print("You entered a negative number!! No conversion for you! \n")
    # else:
    except ValueError:
        print("User input is not a valid number. Try again!! \n")

user_input_message = "Hey!! Enter number of dayys and conversion unit(seperated by : ) \n"   #just a variable