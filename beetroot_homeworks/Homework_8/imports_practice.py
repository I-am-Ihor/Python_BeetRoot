import imported

user_choice = str(input("Do you want know? square room or factorial of number 5? Enter 's' or 'f': "))

if user_choice.lower() == str('s'):
    print("The area of the room is = " + str(imported.my_room_area(5, 7)))

elif user_choice.lower() == str('f'):
    print("the factorial of 5 is = " + str(imported.factorial_number(5)))

else:
    print("Input Error")


