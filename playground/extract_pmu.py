import twixtools
filename = r"D:\testdata\VARIOUS\Siemens\luuk\meas_MID00064_FID204841_wip_039_AdvFlow_BEAT_FQ_dummy.dat"
outfile = r"D:\testdata\VARIOUS\Siemens\luuk\meas_MID00064_FID204841_wip_039_AdvFlow_BEAT_FQ_dummy.pmu"
multi_twix = twixtools.read_twix(filename, include_scans=1, parse_pmu=True, parse_data=False)
twixtools.write_pmu(multi_twix[-1], outfile)