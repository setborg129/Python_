result = []

with open('yrok_6.txt', 'r', encoding='utf-8') as  f:
    for line in f:
        resl = line.find('-')
        data_int = line[:resl -1]  # IP Adress

        resl = line.find('"')
        data_get = line[resl + 1:resl + 4]  # GET

        resl = line.find('GET')
        resl1 = line.find('HTTP')

        data_patch = line[resl + 4: resl1 -1]  # /downloads/product_1
        result.append(f'\n({data_int},{data_get},{data_patch})')




for item in result:
    print(item, end='')
