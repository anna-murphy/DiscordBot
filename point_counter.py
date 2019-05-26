FILE_NAME = "data.dat"

data = {}

class Point_Counter:

    point_data # Dict

    def __init__ (self, file_path):
        with open(file_path) as f:
            for line in f:
                items = line.strip().split(':')
                data[items[0]] = int(items[1])

    def __str__ (self):
        string = ''
        for key in data.keys():
            string.append('{}:{}'.format(key, data[key]))
        return string

    def update(self, name, val):
        if name in data.keys():
            prev_val = data[name]
            data[name] = val + prev_val
        else:
            data[name] = val
        with open(FILE_NAME, "w") as f:
            for name in data.keys():
                f.write("{}:{}\n".format(name, str(data[name])))

def main():
    c = Point_Counter(FILE_NAME)
    c.update('Skitter', 9)

if __name__ == "__main__":
    main()
