import argparse

import twixtools
from pathlib import Path


def find_files_with_extension(directory, extension):
    directory_path = Path(directory)
    file_list = []

    for file_path in directory_path.rglob(f"*{extension}"):
        if file_path.is_file():
            file_list.append(file_path)

    return file_list


parser = argparse.ArgumentParser()
parser.add_argument("dir", help="directory with twix files")

args = parser.parse_args()

target_extension = ".dat"
twix_files = find_files_with_extension(args.dir, target_extension)
for filename in twix_files:
    try:
        pars = twixtools.read_hdr(str(filename))[-1]
    except:
        print(f"Could not read {filename}")
        continue
    study_uid = pars.Config.StudyLOID
    print(study_uid)