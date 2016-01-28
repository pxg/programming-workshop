import datetime
import csv
import sys


def load_csv(file_name):
    output = []
    with open(file_name) as csvfile:
        programs = csv.reader(csvfile, delimiter=',')
        for row in programs:
            output.append((int(row[0]), row[1].strip()))

    return output


def find_program(file_name, timestring):
    data = load_csv(file_name)
    timestamp = parse_timestamp(timestring)
    return current_program(data, timestamp)


def parse_timestamp(timestring):
    timestamp = datetime.datetime.strptime(
        timestring, "%Y-%m-%d %H:%M:%S"
    )
    return int(timestamp.strftime("%s"))


def current_program(data, timestamp):
    found_program = None
    for start_time, prog_name in data:
        if timestamp > start_time:
            found_program = '{} {}'.format(prog_name, timestamp - start_time)

    return found_program

if __name__ == "__main__":
    file_name = str(sys.argv[1])
    prog_time = int(sys.argv[2])
    print "Program starting at {time} according to {f}".format(
        time=prog_time,
        f=file_name,
    )
    print find_program(file_name, prog_time)
