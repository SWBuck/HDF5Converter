from DataType import DataType
from tables import StringCol


class MAP(DataType):
    def __init__(self, p):
        self.data_format = {"chromosome": (0, StringCol(16)), "identifier": (1, StringCol(16)),
                            "distance": (2, StringCol(16)), "position": (3, StringCol(16))}
        DataType.__init__(self, p, "map")

    def __str__(self):
        return self.file_name

    def __repr__(self):
        return self.__str__()
