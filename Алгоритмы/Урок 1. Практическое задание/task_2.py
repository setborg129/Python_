list_item = [6,2,3,5,7,33,1,44,55,11,67,90]

result_min = []
def min_item_square(item_list):                 # !!
    number_result = 99999999999999999
    for itm in item_list:
        for itm2 in item_list:
            if (itm < itm2) :
                if itm < number_result:
                    number_result = itm
    return  number_result



def min_item_line(item_list):          # !
    number_item = 9999999999999999999
    for nums in list_item:
        if nums < number_item:       # !
            number_item = nums
    return number_item



my_list_sq = min_item_square(list_item)
print(f'Минимальное значения из списка {list_item} по квадратному алгоритму  = {my_list_sq}')


my_list_min = min_item_line(list_item) # !
print(f'Минимальное значения из списка {list_item} по линейному алгоритму  = {my_list_min}')







