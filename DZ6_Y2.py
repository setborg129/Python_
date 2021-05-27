from collections import Counter

count = 0
result_spamer = []
with open('yrok_6.txt', 'r', encoding='utf-8') as  f:
    for index, line in enumerate(f):
        count += 1
        resl = line.find('-')
        data_int = line[:resl - 1]  # IP Adress
        result_spamer.append(data_int)

data_spamer = Counter(result_spamer)  # вычисляем дубликаты

count_max = 0
for item in data_spamer:
    if data_spamer[item] > count_max:
        count_max = data_spamer[item]
        ip_adress = item

print(f'IP_Adress спамера: {ip_adress}, колличество запросов: {count_max}')
