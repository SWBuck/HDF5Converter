from os import path


class DataType:
    def __init__(self, file_path, t):
        self.input = file_path
        head, tail = path.split(self.input)
        self.file_name = tail
        self.file_prefix = path.splitext(self.file_name)[0]
        self.type = t

    def read(self):
        with open(self.input) as f:
            for line in f:
                line = line.rstrip().split()
                yield self.formatted_line(line)

    def write(self, table):
        f = []
        for k in self.data_format:
            f.append((k, self.data_format[k][0]))
        a = sorted(f, key=lambda x: x[1])
        with open(self.input, "w") as f:
            for r in table:
                s = ""
                for each in a:
                    s += r[each[0]]+"\t"
                s.strip()
                f.write(s+"\n")

    def formatted_line(self, split_line):
        line_dict = {}
        for k in self.data_format.keys():
            data = split_line[self.data_format[k][0]]
            line_dict[k] = data
        print line_dict
        return line_dict

    def create_table(self, h5_file):
        group_exists = False
        for x in h5_file:
            if x._v_name == self.file_prefix:
                group_exists = True
                group = x
        if not group_exists:
            group = h5_file.create_group("/", self.file_prefix, self.file_prefix)
        table_def = {}
        for k in self.data_format:
            table_def[k] = self.data_format[k][1]
        table = h5_file.create_table(group, self.type, table_def)
        individual = table.row
        for x in self.read():
            for y in x:
                individual[y] = x[y]
            individual.append()
        table.flush()
