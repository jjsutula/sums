import re
import sys


def calculator():

    proceed = True
    while proceed:
        user_in = input("Enter an equation: ")
        if user_in and not user_in.startswith('q'):
            parts = re.findall('[+-/*()]|\d+', user_in)
            print('Parts: '+str(parts))

            left = int(parts[0])
            right = int(parts[2])

            res = doMath(left, parts[1], right)
            print(str(left) + ' ' + parts[1] + ' ' + str(right) + ' = ' + str(res))
        else:
            proceed = False

    print('fin')


def doMath(left, op, right):
    if op == "*":
        return left * right
    elif op == "/":
        return left / right
    elif op == "+":
        return left + right
    else:
        return left - right



def main(argv):
    calculator()

# Do this so that main() only gets called if invoked via command line, but not if invoked programmatically
if __name__ == "__main__":
    main(sys.argv[1:])
