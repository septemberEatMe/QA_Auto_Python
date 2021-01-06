import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--url' '-u',
                    default="22",
                    help="enter you url here")

parser.add_argument("--method", "-m",
                    help="Enter method type",
                    default="GET")

args = parser.parse_args()
print(args)