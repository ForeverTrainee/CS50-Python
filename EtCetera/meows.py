import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
"""
Argparse lesson
We can add program documentation/help notice once program runs: python meows.py --help
We can specify default value, in that example one print by default
Also specify type, in that example int as we need it.
"""
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")