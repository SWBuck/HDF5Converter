from tables import StringCol, open_file
import os


class ConvertPEDMAP:
    def __init__(self, d):
        self.directory = d["dir"]
        self.output = d["output"]
        self.map_files = []
        self.ped_files = []
        self.get_files()
        self.h5_file = open_file(self.output+".h5", mode="w", title="PEDMAP")
        self.ped_group = self.h5_file.create_group("/", "ped", "PED")
        self.map_group = self.h5_file.create_group("/", "map", "MAP")
        self.create_map_tables()
        self.create_ped_tables(self.get_geno_length())
        self.h5_file.close()

    def create_map_tables(self):
        map_table_def = {"chromosome": StringCol(16), "identifier": StringCol(16), "distance": StringCol(16),
                         "position": StringCol(16)}
        for each in self.map_files:
            name = each.replace(self.directory, "").replace(".map", "")
            table = self.h5_file.create_table(self.h5_file.root.map, name, map_table_def)
            individual = table.row
            with open(each) as m:
                for line in m:
                    temp = line.rsplit()
                    individual["chromosome"] = temp[0]
                    individual["identifier"] = temp[1]
                    individual["distance"] = temp[2]
                    individual["position"] = temp[3]
                    individual.append()
            table.flush()

    def create_ped_tables(self, l):
        ped_table_def = {"family": StringCol(16), "sample": StringCol(16), "paternal": StringCol(16),
                         "maternal": StringCol(16), "sex": StringCol(4), "affection": StringCol(16),
                         "genotype": StringCol(l)}
        for each in self.ped_files:
            name = each.replace(self.directory, "").replace(".ped", "")
            table = self.h5_file.create_table(self.h5_file.root.ped, name, ped_table_def)
            individual = table.row
            with open(each) as p:
                for line in p:
                    temp = line.rsplit()
                    individual["family"] = temp[0]
                    individual["sample"] = temp[1]
                    individual["paternal"] = temp[2]
                    individual["maternal"] = temp[3]
                    individual["sex"] = temp[4]
                    individual["affection"] = temp[5]
                    genotype_string = "".join(temp[6:])
                    individual["genotype"] = genotype_string.strip()
                    individual.append()
            table.flush()

    def get_files(self):
        for each in os.listdir(self.directory):
            if each.endswith(".ped"):
                self.ped_files.append(self.directory+each)
            elif each.endswith(".map"):
                self.map_files.append(self.directory+each)

    def get_geno_length(self):
        max_glength = 0
        for each in self.ped_files:
            with open(each) as f:
                    temp = f.readline().rsplit()
                    length = "".join(temp[6:])
                    length = length.strip()
                    if len(length) > max_glength:
                        max_glength = len(length)
        return max_glength