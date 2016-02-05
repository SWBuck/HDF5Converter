from tables import StringCol, open_file


class ConvertPEDMAP:
    def __init__(self, d):
        self.info = d
        self.get_geno_length()
        print "Creating file:", self.info["output"]+".h5"
        self.h5_file = open_file(self.info["output"]+".h5", mode="w", title="PEDMAP")
        self.plink_group = self.h5_file.create_group("/", "plink", "PLINK")
        print "Populating MAP table"
        self.create_map_table()
        print "Populating PED table"
        self.create_ped_table(self.get_geno_length())
        print self.h5_file
        self.h5_file.close()

    def get_geno_length(self):
        with open(self.info["to_prefix"]+".ped") as f:
            temp = f.readline().rsplit()
            length = ""
            for i in xrange(6, len(temp), 2):
                length += temp[i]+""+temp[i+1]+" "
            length = length.strip()
        return len(length)

    def create_ped_table(self, l):
        ped_table_def = {"family": StringCol(16), "sample": StringCol(16), "paternal": StringCol(16),
                         "maternal": StringCol(16), "sex": StringCol(4), "affection": StringCol(16),
                         "genotype": StringCol(l)}
        ped_table = self.h5_file.create_table(self.plink_group, "ped", ped_table_def)
        individual = ped_table.row
        with open(self.info["to_prefix"]+".ped") as p:
            for x in p.readlines():
                temp = x.rsplit()
                individual['family'] = temp[0]
                individual['sample'] = temp[1]
                individual['paternal'] = temp[2]
                individual['maternal'] = temp[3]
                individual['sex'] = temp[4]
                individual['affection'] = temp[5]
                genotype_string = ""
                for index in xrange(6, len(temp), 2):
                    genotype_string += temp[index] + "" + temp[index + 1] + " "
                individual['genotype'] = genotype_string.strip()
                individual.append()
            ped_table.flush()

    def create_map_table(self):
        map_table_def = {"chromosome": StringCol(16), "identifier": StringCol(16), "distance": StringCol(16),
                         "position": StringCol(16)}
        map_table = self.h5_file.create_table(self.h5_file.root.plink, "map", map_table_def)
        individual = map_table.row
        with open(self.info["to_prefix"]+".map") as m:
            for x in m.readlines():
                temp = x.rsplit()
                individual['chromosome'] = temp[0]
                individual['identifier'] = temp[1]
                individual['distance'] = temp[2]
                individual['position'] = temp[3]
                individual.append()
        map_table.flush()
