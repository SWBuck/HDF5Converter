from argparse import ArgumentParser
from pedmap_to_hdf5 import ConvertPEDMAP
from hdf5_to_pedmap import ConvertHDF5


def initialize_graphics():
    print "TD"


def check_args():
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d", "--dir", help="Directory containing PED / MAP files to convert to HDF5", type=str)
    group.add_argument("-f", "--hdf", help = "HDF5 File to convert to PED / MAP files", type=str)
    parser.add_argument("-o", "--output", help="Output file prefix", type=str)
    args = parser.parse_args()
    args_dict = {}
    if args.dir is not None:
        if args.output is None:
            parser.error("-o or --output is required when converting to HDF5")
        else:
            o = args.dir
            if o.endswith("/"):
                args_dict["dir"] = o
            else:
                args_dict["dir"] = o+"/"
            args_dict["output"] = args.output

    elif args.hdf is not None:
        args_dict["hdf"] = args.hdf
    return args_dict


def conversion(d):
    if "hdf" in d:
        print "Convert to PED/MAP"
        convert = ConvertHDF5(d["hdf"])
    if "dir" in d:
        print "Convert to hdf"
        convert = ConvertPEDMAP(d)


if __name__ == "__main__":
    d = check_args()
    conversion(d)
