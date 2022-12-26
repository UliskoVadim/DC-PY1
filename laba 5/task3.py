from random import randint


def get_unique_list_numbers() -> list[int]:
    a = [randint(-10, 10) for _ in range(15)]
    a = set(a)
    while len(a)<15:
        a.add(randint(-10,10))
        a = set(a)
    return a

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))