
# Вариант 1

users_db1 = {'Archi':  ['1ghfyrjkf', 'yes'],
             'Archi1': ['ghfy63kf', 'no'],
             }

def activates(item):
    activ = input(f'Учетная запись {item} не активирована, готовы вы пройти активицию ? (да/нет) : ')
    if activ == 'Да' or activ == 'да':
        activ_quest = input('Сколько будет 2 + 2 =  ')
        if activ_quest == '4':
           print(f'Ваша учетная запись {item} активирована ')
           return 'yes'
    else:
        print(f'Вы отказались от активации учетной записи {item}')
        return 'no'

# Выведем какие учетные записи не активны
print(f'Вариант №1. \nСписок УЗ - {users_db1}')
for indx, item in users_db1.items():                                                    # O(n)
    for item2 in item:
        if item2 == 'no':
            pass
            users_db1[indx][1] = activates(indx)
print(users_db1)


# Вариант 2
usr_db = {'user_test1': {'pass':'fjgyfytj34$', 'active': False},
         }
def find_activ(usr):                                                                    # O(1)
    item_key1 = usr.get('user_test1')                                                   # O(1)
    item_key2 = item_key1.get('active')                                                 # O(1)
    if item_key2 == False:
        edit_key = input(f'Ваша учетная запись не активна, хотите пройти активацию  (да/нет) ? : ')
        if edit_key.lower() == 'да':
            print('Для активации пройдите по ссылке в письме которое отправлено вам на почту ! ')
        elif edit_key.lower() == 'нет':
            print('Вы отказались от активации !')
        else:
            print('Выберене правильный ответ (да/нет)')
print(f'Вариант №2. \n{usr_db} ')
find_activ(usr_db)                                                                          # O(1)


