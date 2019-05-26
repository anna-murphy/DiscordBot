FILE_NAME = "data.dat"

data = {}

class Point_Counter:

    point_data # Dict

    def __init__ (self, file_path):
        with open(file_path) as f:
            for line in f:
                items = line.strip().split(":")
                data[items[0]] = int(items[1])

    def __str__ (self):
        string = ""
        for key in data.keys():
            string.append("{}:{}".format(key, data[key]))
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

    def help (self):
        return "I hear you're looking for help!\n" \
                + "```!p tells you everyone's standing.\n" \
                + "!p l tells you the top 3 people.\n" \
                + "!p username gives the points for a specific user.\n" \
                + "!p username X updates the score for that user.\n" \
                + "```"

    def handle (self, msg):
        contents = msg.strip.split(" ")[1:]
        response = ""
        if len(contents) == 1:
            # printing the score
            pass
        elif len(contents) == 2:
            # either leaderboard, user score, or help
            if contents[1] == "h":
                #help message
                response = self.help();
            elif contens[1] == "l":
                # leader board
                leaders = []
                counter = 1
                for i in sorted (self.point_data):
                    leaders.append(i)
                for u in leaders:
                    response.append("{}. {}\n".format(counter, u))
                    counter += 1
                    if counter == 4:
                        break
            elif contents[1] in self.point_data.keys():
                # user score
                response = "{} has {} points".format(contents[1], self.point_data[contents[1]])
            else:
                # error?
                response = "The formatting of that doesn't feel quite right... try asking for help?"
        elif len(contnets) == 3:
            # update user score
            pass
        else:
            # error
            response = "Uhhh,,, I don't think your message was formatted correctly?" + \
                    "\nMaybe try `!p h` for some help."
        return response

def main():
    c = Point_Counter(FILE_NAME)
    c.update('Skitter', 9)

if __name__ == "__main__":
    main()
