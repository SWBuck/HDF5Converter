from os import listdir
from DataTypes.MAP import MAP
from DataTypes.PED import PED
from DataTypes.HDF5 import HDF5
from tables import open_file


def t():
    input_directory = "/Users/sbuck1994/Documents/Work/HDF5/HDF5Converter/ExampleData/"
    list_files = listdir(input_directory)
    dtypes = {}
    for f in list_files:
        if f.lower().endswith(".map"):
            if "map" not in dtypes:
                dtypes["map"] = []
                dtypes["map"].append(MAP(input_directory+f))
            else:
                dtypes["map"].append(MAP(input_directory+f))

        elif f.lower().endswith(".ped"):
            if "ped" not in dtypes:
                dtypes["ped"] = []
                dtypes["ped"].append(PED(input_directory+f))
            else:
                dtypes["ped"].append(PED(input_directory+f))

    h5_file = open_file("/Users/sbuck1994/Documents/Work/HDF5/HDF5Converter/test.h5", mode="w", title="test")
    for key in dtypes:
        for a in dtypes[key]:
            a.create_table(h5_file)
    h5_file.close()


def f():
    #HDF to ped/map
    import DataTypes.HDF5
    output_dir = "/Users/sbuck1994/Desktop/ED/"
    hdf_file = "/Users/sbuck1994/Documents/Work/HDF5/HDF5Converter/test.h5"
    h = DataTypes.HDF5.HDF5(hdf_file)
    h.convert(output_dir)


## Start CLI ##
import argparse


def initialize_graphics():
    print "ToDo"


def check_args():
    parser = argparse.ArgumentParser(description="HDF5 Converter Command Line Interface")
    parser.add_argument("-v", "--verbose", help="Trigger verbose mode", action="store_true", default=False)
    subparsers = parser.add_subparsers(help="Program mode (i.e. to HDF5 or from HDF5", dest="mode")
    add_convert_to_hdf(subparsers)
    add_convert_from_hdf(subparsers)
    return vars(parser.parse_args())


def add_convert_to_hdf(sp):
    to_parser = sp.add_parser("to", help="Convert files to a single HDF5 file")
    to_parser.add_argument("-d", "--dir", type=str, required=True,
                           help="Directory containing files to convert to HDF5")
    to_parser.add_argument("-o", "--output", type=str, required=True, help="HDF5 output file prefix")


def add_convert_from_hdf(sp):
    from_parser = sp.add_parser("from", help="Convert from HDF5 file")
    from_parser.add_argument("-i", "--hdf", type=str, required=True, help="HDF5 File to convert to multiple files")
    from_parser.add_argument("-d", "--dir", type=str, required=True, help="Directory to save output files to")


def convert_to(a):
    input_directory = a["dir"]
    output_name = a["output"]
    verbose = a["verbose"]
    files = listdir(input_directory)
    dtypes = {}
    for f in files:
        if f.lower().endswith(".map"):
            if "map" not in dtypes:
                dtypes["map"] = []
                dtypes["map"].append(MAP(input_directory+f))
            else:
                dtypes["map"].append(MAP(input_directory+f))
        elif f.lower().endswith(".ped"):
            if "ped" not in dtypes:
                dtypes["ped"] = []
                dtypes["ped"].append(PED(input_directory+f))
            else:
                dtypes["ped"].append(PED(input_directory+f))
    h5_file = open_file(output_name+".h5", mode="w", title=output_name)
    for key in dtypes:
        for a in dtypes[key]:
            a.create_table(h5_file)
    h5_file.close()


def convert_from(a):
    input_file = a["hdf"]
    output_directory = a["dir"]
    verbose = a["verbose"]
    h = HDF5(input_file)
    h.convert(output_directory)


if __name__ == "__main__":
    args = check_args()
    if args["mode"] == "to":
        convert_to(args)
    elif args["mode"] == "from":
        convert_from(args)
