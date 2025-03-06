def contains_sublist(main_list, sublist):

    for i in range(len(main_list) - len(sublist) + 1):
        if main_list[i:i+len(sublist)] == sublist:
            return True
    return False


main_list = [1, 2, 3, 4, 5, 6]
sublist = [3, 4]
result = contains_sublist(main_list, sublist)

if result:
    print(f"The list contains the sublist: {sublist}")
else:
    print(f"The list does not contain the sublist: {sublist}")
