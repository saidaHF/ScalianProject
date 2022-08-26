import csv
import sys

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
        self.filterByValue(CSVData, s1, "entity")
        if s2 is not None:
            self.filterByValue(CSVData, s2, "currency")

    def filterByValue(self, CSVData, s1, value):
        count = 0
        value = value.lower()
        if value not in CSVData[0]:
            raise Exception(f"{value} not found in csv file")
        positionValue = CSVData[0].index(value)
        for i in range(len(CSVData)):
            # CSVData[0] -> la fila entera
            # entity obligatorio:
            if s1 in CSVData[i][positionValue]:
                # print(CSVData[i])  # -> resultado del filtro de entity/currency
                count += 1
        print(f"{s1} is {count} times")
        return CSVData[i]

    def readFileCsv(self, path):
        try:
            with open(path) as file:
                reader = csv.reader(file)
                if not reader:
                    print("There are NOT data in file: " + path)

                CSVData = []
                for row in reader:
                    # CSVData.append([])
                    totalRow = ""
                    for column in row:
                        totalRow += column
                    CSVData.append(totalRow.split(";"))

            return CSVData

        except IOError as e:
            print(f"I/O error({0}): {1}".format(e.errno, e.strerror))


if __name__ == "__main__":
    test = Filter()
    test.loadProgram()
    # test.readFileCsv(aggCSV)
    # test.askParametter()
