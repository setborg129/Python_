import os
from shutil import copyfile


def temp(r_dir):
    print('-1')
    for root, dirs, files in os.walk(r_dir):
        print('0')
        for file in files:
            print('1')
            if file.endswith('.html'):  # Конец_файла
                print('2')
                dir_name = os.path.join('temp_file', os.path.basename(root))
                if not os.path.exists(dir_name):
                    print('3')
                    os.makedirs(dir_name)

                copyfile(os.path.join(root, file), os.path.join(dir_name, file))


if __name__ == '__main__':
    temp(r'my_project')
