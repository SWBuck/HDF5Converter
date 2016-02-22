from tables import open_file
from MAP import MAP
from PED import PED
from os import path, mkdir


class HDF5:
    def __init__(self, name):
        self.h5_file = open_file(name, mode="r")

    def convert(self, directory):
        if not path.exists(directory):
            mkdir(directory)
        for x in self.h5_file.root:
            prefix = x._v_name
            for y in x:
                x = directory+prefix+"."+y._v_name
                if x.lower().endswith(".map"):
                    m = MAP(x)
                    m.write(y)
                elif x.lower().endswith(".ped"):
                    m = PED(x, writing=True)
                    m.write(y)
        self.h5_file.close()
