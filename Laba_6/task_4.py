import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename: str, delimeter: str = ',', new_line: str = '\n') -> list[dict]:
    with open(filename) as f:  # TODO реализовать конвертер из csv в json
        a = []
        for m, n in enumerate(f):
            k = n.strip(new_line).split(delimeter)
            if m == 0:
                z = k
                continue
            a.append({})
            for i, _ in enumerate(z):
                a[-1][z[i]] = k[i]
    return a
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

