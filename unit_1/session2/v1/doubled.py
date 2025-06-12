# Print doubled list

# Understand
    # function takes in a list of ints
    # Even if negative, still ok?
    # Double each int in a list

# Plan
    # Defining list of ints
    # Pass list of integers as parameter to doubled() def
    # Then double each int in list
    # New list is not needed
    # print each doubled item

def doubled(lst):
    if type(lst) != list:
        print("Invalid list")
    else:
        for item in lst:
            # if type(item) != int:
            #     print("Error! List contains some invalid items that are not integers")
            #     break
            # else:
                print(item*2)

lst = [1,2,3]
doubled(lst)