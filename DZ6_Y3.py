from itertools import zip_longest
import sys

def user_with_hobb(hobbies_file, users_file, result_file):
    with open(hobbies_file, 'r', encoding='windows-1251') as hobbies_f, \
         open(users_file,   'r', encoding='windows-1251') as users_f, \
         open(result_file,  'a', encoding='windows-1251') as result_write_f:

        for item, hobbies, in zip_longest(users_f, hobbies_f):
            if item is None:
                exit(1)
            else:
                item = item.strip()
                if hobbies is not None:
                    hobbies = hobbies.strip()
                result_write_f.write(f'{item}: {hobbies}\n')



if __name__ == "__main__":
    _script_name, users_file, hobbies_file, result_file = sys.argv
    user_with_hobb(users_file, hobbies_file,result_file)
