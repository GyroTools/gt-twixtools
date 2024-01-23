import argparse
import twixtools
from twixtools.pmu import _process_pmu

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="twix file")
parser.add_argument("outfile", help="outpuf filename for PMU data")

args = parser.parse_args()

# parse the twix file. PMU data will be in multi_twix[scan_nr]['pmu']
multi_twix = twixtools.read_twix(args.filename, parse_pmu=True, parse_data=False)

# get the first ecg channel
ecg1 = multi_twix[-1]['pmu']['ecg1']

# get the respiratory motion
resp1 = multi_twix[-1]['pmu']['resp1']

# get the pulse plethysmograph
pulse = multi_twix[-1]['pmu']['pulse']

# get the ECG learning data
ecg1_learn = multi_twix[-1]['pmu']['learn']['ecg1']

# write the PMU data to file
twixtools.write_pmu(multi_twix[-1], args.outfile) # write PMU data to file

# read the PMU data from file
pmu = twixtools.read_pmu(args.outfile)
