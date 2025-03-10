import argparse
import expression
parser = argparse.ArgumentParser(description='Genereates a dataset of expressions')
parser.add_argument('--num_ops', type=int, default=5)
parser.add_argument('--items', type=int, default=10)
parser.add_argument('--bins', type=int, default=5)
parser.add_argument('--path_funcs', type=str, default='funcs.csv')
parser.add_argument('--path_hist', type=str, default='hist.csv')
args = parser.parse_args()

expression.gen_dataset(args.num_ops, args.items, (0,1), args.bins, args.path_funcs, args.path_hist)