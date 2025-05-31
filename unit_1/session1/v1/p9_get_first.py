list = [3,1,6,7,5]

def get_first(list):
    if list == None:
        return None
    else:
        first = list[0]
        print(f"Returning first item in list {first}")
        return first

get_first(list)