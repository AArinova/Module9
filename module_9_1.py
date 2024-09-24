def apply_all_func(int_list: list, *functions: list):

    result = dict()

    for i_func in functions:
        result[ i_func.__name__] = i_func(int_list)

    return(result)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))