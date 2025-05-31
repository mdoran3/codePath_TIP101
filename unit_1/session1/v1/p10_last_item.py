list = [3,1,6,7,5]

def get_last(list):
    if list == None:
        return None
    else:
        last = list[len(list) - 1]
        print(f"Returning first item in list {last}")
        return last

get_last(list)