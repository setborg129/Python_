# Вариант 1
my_list = 2345601
result = []
result_old = []
def number_cout(my_lst):
    result_str = map(int, str(my_lst))
    for nums in result_str:
        if nums % 2 == 0:
            result.append(nums)
        else:
            result_old.append(nums)
    print(f'Список четных чисел  = {result}')
    print(f'Список НЕ четных чисел  = {result_old}')

print('Вариант № 1 - цикл')
number_cout(my_list)


# Вариант 2   Рекурсия
lv_result1 = []
old_result1 = []
def number_cout2(my_lst):                               # (O(n^2))

    if my_lst == 0:
        print(f'Список четных чисел  = {lv_result1}')
        print(f'Список НЕ четных чисел  = {old_result1}')
        exit()

    lv_result = my_lst % 10
    if lv_result % 2 == 0:
        lv_result1.append(lv_result)                        # O(1)
        my_lst = my_lst // 10
        number_cout2(my_lst)
    else:
        old_result1.append(lv_result)                       # O(1)
        my_lst = my_lst // 10
        number_cout2(my_lst)


print('Вариант № 2 - Рекурсия')
number_cout2(my_list)