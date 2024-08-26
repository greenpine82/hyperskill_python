import argparse
from math import ceil, log
import sys


def validate_argument(args):
    is_invalid = (args.type not in ('annuity', 'diff')
                  or args.payment < 0 or args.principal < 0 or args.periods < 0
                  or args.interest <= 0
                  or (args.type == 'diff' and args.payment))
    if is_invalid:
        print('Incorrect parameters')
        sys.exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str, default='None')
    parser.add_argument("--payment", type=float, default=0.0)
    parser.add_argument("--principal", type=int, default=0)
    parser.add_argument("--periods", type=int, default=0)
    parser.add_argument("--interest", type=float, default=0.0)
    args = parser.parse_args()

    validate_argument(args)
    
    i = args.interest / 1200
    periods = args.periods
    principal = args.principal
    payment = args.payment
    if args.type == 'diff':
        total = 0
        for m in range(periods):
            d = ceil(principal / periods + i * (principal * (periods - m) / periods))
            print(f'Month {m + 1}: payment is {d}')
            total += d
        print("")
        print(f'Overpayment = {total - principal}')
    elif principal == 0:
        principal = round(payment / (i * ((1 + i) ** periods) / (((1 + i) ** periods) - 1)))
        print(f'Your loan principal = {principal}!')
        print(f'Overpayment = {payment * periods - principal}')
    elif periods != 0:
        payment = ceil(principal * i * ((1 + i) ** periods) / (((1 + i) ** periods) - 1))
        print(f'Your annuity payment = {payment}!')
        print(f'Overpayment = {payment * periods - principal}')
    else:
        t  = ceil(log(payment / (payment - (i * principal)), 1 + i))
        y, m = divmod(t, 12)

        years = f"{y} year{'s' if y > 1 else ''} " if y > 0 else ""

        months = f"{m} month{'s' if m > 1 else ''} " if m > 0 else ""

        time = years + ('and ' if y > 0 and m > 0 else '') + months
    
        print(f'It will take {time}to repay this loan!')
        print(f'Overpayment = {ceil(payment) * t - principal}')