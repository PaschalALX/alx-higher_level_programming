#!/usr/bin/python3
if __name__ == "__main__":

    from sys import argv, exit

    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if not (argv[2] in '+-*/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    from calculator_1 import add, sub, mul, div

    z = {
        "x": int(argv[1]),
        "y":  int(argv[3]),
        "opr": argv[2],
        "res": 0
    }

    if z['opr'] == '+':
        z['res'] = add(z['x'], z['y'])
    elif z['opr'] == '-':
        z['res'] = sub(z['x'], z['y'])
    elif z['opr'] == '*':
        z['res'] = mul(z['x'], z['y'])
    elif z['opr'] == '/':
        z['res'] = div(z['x'], z['y'])

    print("{x} {opr} {y} = {res}".format(**z))
