import argparse
import math
import sys


def validate_argument(args):
    is_invalid = args.type not in ('annuity', 'diff')
    is_invalid = is_invalid or args.payment < 0 or args.principal < 0 or args.periods < 0
    is_invalid = is_invalid or args.interest <= 0
    is_invalid = is_invalid or (args.type == 'diff' and args.payment)
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
    if args.type == 'diff':
        total = 0
        for m in range(0, args.periods):
            d = args.principal / args.periods + i * (args.principal * (args.periods - m) / args.periods)
            print(f'Month {m + 1}: payment is {math.ceil(d)}')
            total += math.ceil(d)
        print("")
        print(f'Overpayment = {total - args.principal}')
    elif args.principal == 0:
        principal = args.payment / (i * ((1 + i) ** args.periods) / (((1 + i) ** args.periods) - 1))
        print(f'Your loan principal = {round(principal)}!')
        print(f'Overpayment = {args.payment * args.periods - round(principal)}')
    elif args.periods != 0:
        payment = args.principal * i * ((1 + i) ** args.periods) / (((1 + i) ** args.periods) - 1)
        print(f'Your annuity payment = {math.ceil(payment)}!')
        print(f'Overpayment = {math.ceil(payment) * args.periods - args.principal}')
    else:
        t  = math.log(args.payment / (args.payment - (i * args.principal)), 1 + i)
        y, m = divmod(math.ceil(t), 12)

        years = f"{y} year{'s' if y > 1 else ''} " if y > 0 else ""

        months = f"{m} month{'s' if m > 1 else ''} " if m > 0 else ""

        time = years + 'and ' if y > 0 and m > 0 else '' + months
    
        print(f'It will take {time}to repay this loan!')
        print(f'Overpayment = {math.ceil(args.payment) * math.ceil(n) - args.principal}')