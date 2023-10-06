#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] == '+':
            result = add(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '-':
            result = sub(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '/':
            result = div(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '*':
            result = mul(int(sys.argv[1]), int(sys.argv[3]))
    else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {result}")
