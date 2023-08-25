"""
Complete create_parser below so that our BMI program can be called like this:

$ python bmi.py -h
usage: bmi.py [-h] [-w WEIGHT] [-l LENGTH]

Calculate your BMI.

optional arguments:
  -h, --help            show this help message and exit
  -w WEIGHT, --weight WEIGHT
                        Your weight in kg
  -l LENGTH, --length LENGTH
                        Your length in cm

$ python bmi.py -w 80 -l 187
Your BMI is: 22.88
"""

import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="Calculate your BMI.")
    
    parser.add_argument("-w", "--weight", type=float, help="Your weight in kg")
    parser.add_argument("-l", "--length", type=int, help="Your length in cm")

    return parser


def calc_bmi(weight, length):
    # BMI calculation logic
    bmi = weight / ((length/100) ** 2)
    return bmi

def handle_args(args):
    if args.weight is None or args.length is None:
        print("Both weight and length are required to calculate BMI")
        return
        # purpose of using return statement is to exit the function early in case the required args are not provided by the user.
        # it terminates the function execution without performing the BMI calculation if the necessary args are missing.
    
    bmi = calc_bmi(args.weight, args.length)
    print("Your BMI is: {:.2f}".format(bmi))


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    handle_args(args)