from tables import open_file


class ConvertHDF5:
    def __init__(self, d):
        self.h5_file = open_file(d)
        self.create_map_files()
        self.create_ped_files()
        self.h5_file.close()

    def create_map_files(self):
        for each in self.h5_file.root.map:
            name = each._v_name+".map"
            with open(name, "w") as m:
                for r in each:
                    m.write(r['chromosome'] + "\t" + r['identifier'] + "\t" + r['distance'] + "\t" + r['position'] +
                            "\n")

    def create_ped_files(self):
        for each in self.h5_file.root.ped:
            name = each._v_name+".ped"
            with open(name, "w") as m:
                for r in each:
                    geno = " ".join(r["genotype"])
                    m.write(r['family'] + "\t" + r['sample'] + "\t" + r['paternal'] + "\t" + r['maternal'] + "\t" +
                            r['sex'] + "\t" + r['affection'] + "\t" + geno + "\n")
