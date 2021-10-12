reslt = 0

def resiver(number):
    # res_str = len(str(res))


    res_str = len(str(number))
    if res_str == 1:
        return
    else:
        num = int(number)

        result_int = num % 10
        num = num // 10
        resiver(num)


num = int(input('Ввидите 3-4 значное число '))
print(f'Пользователь ввел число {num}')
resiver(num)