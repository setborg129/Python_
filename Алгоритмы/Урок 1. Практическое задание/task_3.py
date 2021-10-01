my_dict = {'SurgutNeftigas': 8881111, 'Lukoil': 5433, 'TransNeft': 444434}
result = {}
# Вариант первый
def find_max(l_dict):                   # O(1)
    result_find_item = 0
    for item in l_dict.keys():          # O(N)
        find_num = my_dict[item]
        if find_num > result_find_item:
            result_find_item = find_num
            result.clear()               #O(1)
            result[item] = find_num      #O(1)
    return result


max_number = find_max(my_dict)           #O(1)
print(f'Максимальная годовая прибыль  =  {max_number}') #O(1)


# Вариант второй

result_dict_2 = dict([max(my_dict.items(), key=lambda k_v: k_v[1])])     #O(N)  Линейный поиск
print(f'Максимальная годовая прибыль  =  {result_dict_2}')               #O(1)


# Вариант третий

result_dict_3 = sorted(my_dict, key=my_dict.__getitem__)                  #O(n Log n)
k = result_dict_3[-1]                                                     #O(1)
{k: my_dict[k]}                                                           #O(1)
print(f'Максимальная годовая прибыль в компании {k} = {my_dict[k]}')      #O(1)

# Я считаю что самый просто без заморочек поиск с максимальной прибылью это 3-й вариант, так как вычисления идут только по сортировке.
# Вариант 1 - это уже чисто мое личное мышление по поиску максимальных значений + добавление результата в новый список.
# Вариант 2 - самый трудоемкий и затратный по ресурсам, так как используется  функция словаря, максимума и лямбды ))) 