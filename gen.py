import itertools

bounds = 100

def actual(num: int, op: str, num2: int):
    if op == '+':
        return num + num2
    elif op == '-':
        return num - num2
    elif op == '*':
        return num * num2
    elif op == '/':
        try:
            return num / num2
        except ZeroDivisionError:
            return 'undefined'

with open("tempfile.txt", 'w') as f:
    for x, y, op in itertools.product(range(-1 * bounds, bounds), range(-1 * bounds, bounds), '+-*/'):
        f.write(f"    if n1 == '{x}' and op == '{op}' and n2 == '{y}':\n        result = '{actual(x, op, y)}'\n")
        # print(x, y)

