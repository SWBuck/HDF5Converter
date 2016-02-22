from os import listdir
from DataTypes.MAP import MAP
from DataTypes.PED import PED
from tables import open_file

input_directory = "/Users/sbuck1994/Documents/Work/HDF5/HDF5Converter/ExampleData/"

list_files = listdir(input_directory)
dtypes = {}
unknown_type = []
for f in list_files:
    if f.endswith(".map"):
        if "map" not in dtypes:
            dtypes["map"] = []
            dtypes["map"].append(MAP(input_directory+f))
        else:
            dtypes["map"].append(MAP(input_directory+f))

    elif f.endswith(".ped"):
        if "ped" not in dtypes:
            dtypes["ped"] = []
            dtypes["ped"].append(PED(input_directory+f))
        else:
            dtypes["ped"].append(PED(input_directory+f))

#h5_file = open_file("/Users/sbuck1994/Documents/Work/HDF5/HDF5Converter/test.h5", mode="w", title="test")
#for key in dtypes:
#    for a in dtypes[key]:
#        a.create_table(h5_file)
#h5_file.close()


#HDF to ped/map
import DataTypes.HDF5
output_dir = "/Users/sbuck1994/Desktop/ED/"
hdf_file = "/Users/sbuck1994/Documents/Work/HDF5/HDF5Converter/test.h5"
h = DataTypes.HDF5.HDF5(hdf_file)
h.convert(output_dir)

