from argparse import ArgumentParser
from pedmap_to_hdf5 import ConvertPEDMAP
import hdf5_to_pedmap


def initialize_graphics():
    print "ToDo"


def check_args():
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-t", "--tohdf5", help="PED / MAP file prefix to convert to HDF5", type=str)
    group.add_argument("-f", "--fromhdf5", help="HDF5 file to convert to PED / MAP", type=str)
    parser.add_argument("-o", "--output", help="Output file prefix", type=str, required=True)
    args = parser.parse_args()
    args_dict = {"output": args.output}
    if args.tohdf5:
        print "Converting", args.tohdf5+".map and "+args.tohdf5+".ped", "to",args.output+".h5"
        args_dict['to_prefix'] = args.tohdf5
    elif args.fromhdf5:
        print "Converting", args.fromhdf5, "to", args.output+".h5"
        args_dict["from_file"] = args.fromhdf5
    return args_dict


def conversion(dict):
    if "to_prefix" in dict:
        converter = ConvertPEDMAP(dict)
    elif "from_file" in dict:
        print "hdf5_to_pedmap"


if __name__ == "__main__":
    d = check_args()
    conversion(d)
