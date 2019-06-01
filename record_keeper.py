"""
    File: record_keeper.py
    Author: Anna Murphy
"""

class Record_Keeper:

    def __init__ (self):
        pass

class Record:

    date = ""
    points = 0
    author = ""
    location = ""

    def __init__ (self,\
            location):
        self.location = location
        with open(self.location, "r") as f:
            self.author = f.readline().strip()
            self.date = f.readline().strip()
            try:
                self.points = int(f.readline().strip())
            except:
                self.points = 0

    def contents (self):
        contents = ""
        with open(self.location, "r") as f:
            counter = 0
            for line in f:
                if counter <=2:
                    # Skip the first 4 lines,
                    # author, date, & points
                    pass
                else:
                    content += f.readline()
                counter += 1
            return content

    def __str__ (self):
            return self.author " on " + self.date + \
                    ":```" + self.contents() + "```"
