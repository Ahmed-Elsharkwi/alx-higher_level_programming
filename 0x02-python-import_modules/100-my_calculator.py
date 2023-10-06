#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    match sys.argv[2]:
        case '+':
            result = add(int(sys.argv[1]), int(sys.argv[3]))
        case '-':
            result = sub(int(sys.argv[1]), int(sys.argv[3]))
        case '/':
            result = div(int(sys.argv[1]), int(sys.argv[3]))
        case '*':
            result = mul(int(sys.argv[1]), int(sys.argv[3]))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {result}")
