import argparse
import sys
import pdb

print(str(sys.argv))

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('testrun', type=str, nargs=1,
                    help='Testrun name')
parser.add_argument('job', type=str, nargs=1,
                    help='Jenkins job name')
parser.add_argument('timestamp', type=str, nargs=1,
                    help='Unix timestamp')
parser.add_argument('build', type=str, nargs=1,
                    help='Build number')
parser.add_argument('--tvapp-perf-test', dest='tvapp-perf-test', action='store_true')

args = parser.parse_args()
print(args)
pdb.set_trace()

