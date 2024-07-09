#import helper_basic      #importing the file which has all the functions defined
from helper_basic import validate_and_execute,user_input_message   #this is used when particularly only one specific function is needed in main file

user_input = ""
while user_input != "exit":
    # user_input = input ("Hey! Enter a number as a comma seperated list!\n")
    # for num_of_days_element in set(user_input.split(",")):  #split() is a function which converts string to list datatype(as user_input is a string)
    #                                                         #set(....) converts the list to set => removes the duplicate elements(if present)
    #     validate_and_execute()

    user_input = input(user_input_message)  #list created
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    #creation of dictionary
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    # helper_basic.validate_and_execute(days_and_unit_dictionary)      #calling validate_and_execute function from helper_basic file
    validate_and_execute(days_and_unit_dictionary)          #if from is used, then we donot need to modularize the function

print("Program executed successfully \n")


