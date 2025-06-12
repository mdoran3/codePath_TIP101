def print_list(lst):
    if type(lst) != list:
        print("Invalid list")
    else:
        for item in lst:
            print(item)

lst = ["squirtle", "gengar", "charizard", "pikachu"]

#print_list(1)
print_list(lst)