"""
    File: record_keeper.py
    Author: Anna Murphy
"""

class Record_Keeper:

    LOCATION = "records/"

    by_author = {}
    by_date = []
    by_points = []

    def __init__ (self, directory):
        for record_file in directory:
            record = Record(record_file)
            self.by_author[record.author] = record
            self.by_date.append(record)
            self.by_points.append(record)
        self.sort_collections()

    def __str__ (self):
        return "Records in /" + \
                LOCATION + " holding " + \
                str(len(self.by_date)) + " records."

    def sort_collections (self):
        self.by_date.sort(key=lambda x: x.date)
        self.by_points.sort(key=lambda x: x.points)

    def add_record (self, author,\
            date, points, content):
        filename = LOCATION + author + "_" + date + "_" + points + ".rec"
        with open(filename, "w") as new_record:
            new_record.writeline(author)
            new_record.writeline(date)
            new_record.writeline(points)
            new_record.writeline(content)
        new_record = Record(filename)
        self.by_author[filename.author] = new_record
        self.by_date.append(new_record)
        self.by_points.append(new_record)
        self.sort_collections()

    def get_author_recent (self, author):
        pass

    def get_author_top (self, author):
        pass

    def get_top_all_time (self):
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
