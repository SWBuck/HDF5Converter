from DataType import DataType
from tables import StringCol


class PED(DataType):
    def __init__(self, p, writing=False):
        self.input = p
        self.data_format = {"family": (0, StringCol(16)), "sample": (1, StringCol(16)), "paternal": (2, StringCol(16)),
                                "maternal": (3, StringCol(16)), "sex": (4, StringCol(4)), "affection": (5, StringCol(16))}
        if not writing:
            self.geno_length = self.get_geno_length()
            self.data_format["genotype"] = (6, StringCol(self.geno_length))
        else:
            self.data_format["genotype"] = (6, StringCol(4))
        DataType.__init__(self, p, "ped")

    def __str__(self):
        return self.file_name

    def __repr__(self):
        return self.__str__()

    def write(self, table):
        f = []
        for k in self.data_format:
            f.append((k, self.data_format[k][0]))
        a = sorted(f, key=lambda x: x[1])
        with open(self.input, "w") as f:
            for r in table:
                s = ""
                geno = " ".join(r["genotype"])
                for each in a:
                    if not each[0] == "genotype":
                        s += r[each[1]]+"\t"
                    else:
                        s += geno + "\t"
                s.rstrip()
                f.write(s+"\n")

    def formatted_line(self, split_line):
        line_dict = {}
        for k in self.data_format.keys():
            if k == "genotype":
                x = self.data_format[k][0]
                geno_string = "".join(split_line[x:])
                line_dict[k] = geno_string.strip()
            else:
                data = split_line[self.data_format[k][0]]
                line_dict[k] = data
        return line_dict

    def get_geno_length(self):
        with open(self.input) as f:
            line = f.readline().rsplit()
            length_string = "".join(line[6:])
            length_string = length_string.rstrip()
            max_glength = len(length_string)
        return max_glength

