import os, csv, argparse

parser = argparse.ArgumentParser(description='CSV divider app')
group = parser.add_mutually_exclusive_group()
group.add_argument('-c', '--count', dest="count", action='store')
group.add_argument('-p', '--part', dest="part", action='store')

parser.add_argument('-f', '--file', dest="file", action='store', required=True)
parser.add_argument('-n', '--name', dest="name", action='store', required=True)
parser.add_argument('-nh','--noheader', dest="header", action='store_true')
arguments = parser.parse_args()

file = arguments.file
name = arguments.name
part = arguments.part
count = arguments.count

if count:
        reader = csv.reader(open(file))
        rows = list(reader)
        total_count = len(rows)
        part_count = (total_count + int(count)) // int(count)
        print("\tTotal size: " + str(total_count) + " rows")
        print("\tPart count: " + str(part_count) + " parts")
        print("\tPart size: " + str(count) + " rows")

        reader = csv.reader(open(file))
        writers = []
        headers = None
        if not arguments.header:
            print("\tDuplicating headers")
            headers = next(reader)
        else:
            print("\tNot duplicating headers")

        for i in range(int(part_count)):
            writers.append(csv.writer(open(name + "_" + str(i+1) + '.csv', 'w'), delimiter=','))

        writer = writers[0]
        if headers:
            writer.writerow(headers)

        counter = 0
        for i, row in enumerate(reader):
            if i < int(count) * (counter + 1):
                writer.writerow(row)
            else:
                counter += 1
                writer = writers[counter]
                if headers:
                    writer.writerow(headers)

elif part:
    reader = csv.reader(open(file))
    rows = list(reader)
    total_count = len(rows)
    part_size = (total_count + int(part)) // int(part)
    print("\tTotal size: " + str(total_count) + " rows")
    print("\tPart count: " + str(part) + " parts")
    print("\tPart size: " + str(part_size) + " rows")

    reader = csv.reader(open(file))
    writers = []
    headers = None
    if not arguments.header:
        print("\tDuplicating headers")
        headers = next(reader)
    else:
        print("\tNot duplicating headers")

    for i in range(int(part)):
        writers.append(csv.writer(open(name + "_" + str(i+1) + '.csv', 'w'), delimiter=','))

    writer = writers[0]
    if headers:
        writer.writerow(headers)

    count = 0
    for i, row in enumerate(reader):
        if i < part_size * (count + 1):
            writer.writerow(row)
        else:
            count += 1
            writer = writers[count]
            if headers:
                writer.writerow(headers)
