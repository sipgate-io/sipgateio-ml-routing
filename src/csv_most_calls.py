import csv
import sys

class CsvEntry():
    masterSipID: str
    source: str
    target: str
    seconds: str
    date: str

    def __init__(self, source, target, seconds, date, masterSipID):
        self.source = source
        self.target = target
        self.seconds = seconds
        self.date = date
        self.masterSipID = masterSipID

file_path = sys.argv[1]

def read_line(line) -> CsvEntry:
    return CsvEntry(source = line[16], target = line[17], seconds= line[20], date=line[22], masterSipID=line[2])

with open(file_path, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar='"')
    # erste Zeile (den CSV-Header) überspringen
    reader.__next__()

    callsPerCustomer = {}

    for line in reader:
        entry = read_line(line)

        try:
            callsPerCustomer[entry.masterSipID] += 1
        except:
            callsPerCustomer[entry.masterSipID] = 1

    callsPerCustomerSorted = sorted(callsPerCustomer.items(), key=lambda item: item[1])

    for i in range(len(callsPerCustomerSorted)):
        print(callsPerCustomerSorted[-(i + 1)])
