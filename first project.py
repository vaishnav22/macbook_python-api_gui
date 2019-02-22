def switch_if():
    value1 = int(input("enter the first value: "))
    value2 = int(input("enter the second value: "))
    print("press one for additon \n press 2 for subtraction \n press 3 for multiplication \n press 4 for devison \n ")
    option = int(input("OPTION PLEASE: "))

    if option == 1:
        print("you have choose addition!!")
        value = value1 + value2
        print("value is ",value)

    elif option == 2:
        print("you have choose subtraction!!")
        value = value1 - value2
        print("value is ", value)

    elif option == 3:
        print("you have choose multiplication!!")
        value = value1 * value2
        print("value is ", value)

    elif option == 4:
        print("you have choose devison!")
        value = value1/ value2
        print("value is ", value)

    else:
        print("invalid option")

switch_if()
