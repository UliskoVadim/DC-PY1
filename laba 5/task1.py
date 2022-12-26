from pprint import pprint

empty_list = []
i = 0
while i <= 15:
    dict_of_i = {
        'bin' : bin(i),
        'dec': i,
        'hex' : hex(i),
        'oct': oct(i),
    }
    list_ = [dict_of_i]
    empty_list += list_
    i += 1
pprint(empty_list)

