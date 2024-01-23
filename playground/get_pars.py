import argparse
import twixtools

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="twix file")

args = parser.parse_args()

pars = twixtools.read_hdr(args.filename)[-1]
study_uid = pars.Config.StudyLOID
print(study_uid)
study_uid2 = pars.get('StudyLOID')
print(study_uid2)
study_uid3 = pars.get('StudyLOI', default='123')
print(study_uid3)