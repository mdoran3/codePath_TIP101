def common_keys(dict1, dict2):
	common_list = []
	for key in dict1:
		if key in dict2:
			common_list.append(key)
	return common_list

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)