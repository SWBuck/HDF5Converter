from tables import open_file


class ConvertHDF5:
    def __init__(self, d):
        self.info = d
        self.h5_file = open_file(self.info["from_file"])
        self.create_map_file()
        self.create_ped_file()
        self.h5_file.close()

    def create_map_file(self):
        with open(self.info["output"]+".map", mode="w") as m:
            for r in self.h5_file.root.plink.map:
                m.write(r['chromosome'] + "\t" + r['identifier'] + "\t" + r['distance'] + "\t" + r['position'] + "\n")

    def create_ped_file(self):
        with open(self.info["output"]+".ped", mode="w") as p:
            for r in self.h5_file.root.plink.ped:
                geno = " ".join(r["genotype"])
                p.write(r['family'] + "\t" + r['sample'] + "\t" + r['paternal'] + "\t" + r['maternal'] + "\t" +
                        r['sex'] + "\t" + r['affection'] + "\t" + geno + "\n")
