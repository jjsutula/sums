import argparse
import sys


def compute_temps(temperature, direction):
    if direction == 'ftoc':
        value = (temperature - 32) * 5/9
        out = "%d Fahrenheit is %d Celsius" % (temperature, value)
    else:
        value = (9/5 * temperature) + 32
        out = "%d Celsius is %d Fahrenheit" % (temperature, value)

    print(out)


def main(argv):
    parser = argparse.ArgumentParser(prog='temps', description='Convert between Fahrenheit and Celsius')
    parser.add_argument('-t', '--temperature', required=True, type=int, help='the value to convert')
    parser.add_argument('-d', '--dir', type=str, default='ftoc', help='ctof are converting FROM c to f, ftoc if you are converting TO f from c')
    args = parser.parse_args()

    compute_temps(args.temperature, args.dir)

# Do this so that main() only gets called if invoked via command line, but not if invoked programmatically
if __name__ == "__main__":
    main(sys.argv[1:])
