def remove_duplicates(test_list):
    # using naive method
    # to remove duplicated
    # from list
    res = []
    for i in test_list:
        if i not in res:
            res.append(i)
    return res


test_list = [1, 3, 5, 6, 3, 5, 6, 1]
print("The original list is : " + str(test_list))
print("The list after removing duplicates : " + str(remove_duplicates(test_list)))