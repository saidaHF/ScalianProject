import csv
import sys
import logging
import MySQLdb
import errno
from os import mkdir
from datetime import datetime

aggCSV = "./resources/agg.csv"
mvtCSV = "./resources/mvt.csv"


class Filter:
    def __init__(self):
        self.CSVDataAgg = self.readFileCsv(aggCSV)
        self.CSVDataMvt = self.readFileCsv(mvtCSV)

    def loadProgram(self):
        self.configureLogs()
        self.checkParameters()
        # self.resultFilterAgg = \
        print("Filter AGG:")
        CSVDataAgg = self.filterByEntityAndCurrency(self.CSVDataAgg)
        # self.resultFilterMvt = \
        print("Filter MVT:")
        CSVDataMvt = self.filterByEntityAndCurrency(self.CSVDataMvt)
        print("Filter -> in mvt status != expected:")
        self.filterByValue(CSVDataMvt, "expected", "status", False)
        print("Filter -> in agg value true in isTotalCash and statusLiq != expected:")
        self.filterByValue(CSVDataAgg, "true", "isTotalCash", True)

    def configureLogs(self):
        try:
            mkdir('logs')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise Exception(e)
        pathLogFile = "./logs/" + datetime.today().strftime('%Y-%m-%d_%H_%M_%S') + ".log"
        logging.basicConfig(filename=pathLogFile, encoding='utf-8', level=logging.DEBUG)
    def checkParameters(self):
        logging.info("Checking if all parameters are correct")
        if len(sys.argv) < 2:
            logging.error("Parameters not found")
            raise Exception("You need 'entity' parameter")
        if len(sys.argv) > 3:
            logging.error("Found too many parameters")
            raise Exception("Too many parameters. Check out!")
        logging.info("Loading parameters correct")

    def filterByEntityAndCurrency(self, CSVData):
        parameterEntity, parameterCurrency = sys.argv[1], sys.argv[2]
        if parameterEntity is None:
            print("Please, add the first parameter 'entity': ")
            logging.error("Parameter 'entity' not detected. The aplication need this parameter.")
        CSVData = self.filterByValue(CSVData, parameterEntity, "entity", True)
        if parameterCurrency is not None:
            CSVData = self.filterByValue(CSVData, parameterCurrency, "currency", True)
        return CSVData

    def filterByValue(self, CSVData, value, nameColumn, isContainValue):
        count = 0  # for test
        nameColumn = nameColumn.lower()

        CSVDataNew = []
        # CSVData[0] is always the header
        CSVDataNew.append(CSVData[0])

        if nameColumn not in CSVData[0]:
            logging.error("Not found value in CSV file")
            raise Exception(f"{nameColumn} not found in csv file")

        positionColumn = CSVData[0].index(nameColumn)

        for i in range(1, len(CSVData)):
            # CSVData[0] -> all row
            if isContainValue:
                if value in CSVData[i][positionColumn]:
                    count += 1
                    CSVDataNew.append(CSVData[i])
            else:
                if value != CSVData[i][positionColumn]:
                    print(CSVData[i])
                    count += 1
                    CSVDataNew.append(CSVData[i])
        print(f"{value} is {count} times")
        return CSVDataNew

    def readFileCsv(self, path):
        try:
            with open(path) as file:
                reader = csv.reader(file)
                if not reader:
                    logging.error(f"There are NOT data in file: {path}")
                CSVData = []
                for row in reader:
                    totalRow = ""
                    for column in row:
                        totalRow += column
                    CSVData.append(totalRow.split(";"))
            return CSVData
#
        except IOError as e:
            logging.error(f"I/O error({0}): {1}".format(e.errno, e.strerror))


if __name__ == "__main__":
    filter = Filter()
    filter.loadProgram()
