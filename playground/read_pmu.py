import argparse
import twixtools

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="pmu file")

args = parser.parse_args()

pmu = twixtools.read_pmu(args.filename)
pass