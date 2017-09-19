import argparse

def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("<salesmen>", type=check_positive, help="number of salesmen as a positive number (e.g: \"1\" or \"42\")")
    args = parser.parse_args()
    return args

def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
         raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue
