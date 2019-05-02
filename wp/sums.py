import sys


def compute_sums():
    matches = []

    for hundreds in range(10):
        for tens in range(10):
            for ones in range(10):
                target = hundreds*100 + tens*10 + ones
                value = hundreds ** 3
                if value <= target:
                    value += tens ** 3
                    if value <= target:
                        value += ones ** 3
                        if value == target:
                            matches.append(target)

    print('Found '+str(len(matches))+' items:')
    for m in matches:
        print('  '+str(m))



def main(argv):
    compute_sums()

# Do this so that main() only gets called if invoked via command line, but not if invoked programmatically
if __name__ == "__main__":
    main(sys.argv[1:])
