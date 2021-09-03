def get_max_min(data_list):
    max_value = max(data_list)
    min_value = min(data_list)

    return(max_value, min_value)

max_value, min_value = get_max_min([1,2,3,4,5])
print(max_value)
print(min_value)