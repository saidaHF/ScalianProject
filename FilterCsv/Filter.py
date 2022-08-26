import csv
import sys
import logging
from os import mkdir
import errno
from datetime import datetime

aggCSV = "./resources/agg.csv"
mvtCSV = "./resources/mvt.csv"


class Filter:
    def __init__(self):
        self.CSVDataAgg = self.readFileCsv(aggCSV)
        self.CSVDataMvt = self.readFileCsv(mvtCSV)

    def loadProgram(self):
        self.filterByEntityAndCurrency(self.CSVDataAgg)
        self.filterByEntityAndCurrency(self.CSVDataMvt)

    def filterByEntityAndCurrency(self, CSVData):
        s1, s2 = sys.argv[1], sys.argv[2]
        if s1 is None:
            print("Please, add the first parameter 'entity': ")
            logging.error("ERROR: Parameter 'entity' not detected. The aplication need this parameter.")
        self.filterByValue(CSVData, s1, "entity")
        if s2 is not None:
            self.filterByValue(CSVData, s2, "currency")

    def filterByValue(self, CSVData, value, nameColumn):
        isEquals = False
        count = 0
        nameColumn = nameColumn.lower()
        if nameColumn not in CSVData[0]:
            logging.error("ERROR: Not found value in CSV file")
            raise Exception(f"{nameColumn} not found in csv file")
        positionColumn = CSVData[0].index(nameColumn)
        for i in range(len(CSVData)):
            # CSVData[0] -> all row
            # entity is obligatory:
            if isEquals:
                if value in CSVData[i][positionColumn]:
                    # print(CSVData[i])  # -> resultado del filtro
                    count += 1
            else:
                if value not in CSVData[i][positionColumn]:
                    # print(CSVData[i])  # -> resultado del filtro
                    # status not expected
                    count += 1

        print(f"{value} is {count} times")
        return CSVData[i]

    def readFileCsv(self, path):
        try:
            with open(path) as file:
                reader = csv.reader(file)
                if not reader:
                    print(f"There are NOT data in file: {path}")
                CSVData = []
                for row in reader:
                    totalRow = ""
                    for column in row:
                        totalRow += column
                    CSVData.append(totalRow.split(";"))
            return CSVData

        except IOError as e:
            print(f"I/O error({0}): {1}".format(e.errno, e.strerror))


if __name__ == "__main__":
    try:
        mkdir('logs')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    pathLogFile = "./logs/" + datetime.today().strftime('%Y-%m-%d_%H_%M_%S') + ".log"
    logging.basicConfig(filename=pathLogFile, encoding='utf-8', level=logging.DEBUG)
    # logging.debug('This message should go to the log file')
    # logging.info('So should this')
    # logging.warning('And this, too')
    # logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
    filter = Filter()
    filter.loadProgram()
    # test.readFileCsv(aggCSV)
    # test.askParametter()
