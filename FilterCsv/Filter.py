import csv
import sys

aggCSV = "./resources/agg.csv"
mvtCSV = "./resources/mvt.csv"


class Filter:
    def __init__(self):

        self.CSVDataAgg = self.readFileCsv(aggCSV)
        self.CSVDataMvt = self.readFileCsv(mvtCSV)

    def loadProgram(self):
        s1, s2 = sys.argv[1], sys.argv[2]
        if s1 is None:
            print("Please, add the first parameter 'entity': ")
        self.filterChoice(self.CSVDataAgg, s1, s2)
        # self.filterChoice(CSVDataMvt, s1, s2)

    def filterChoice(self, CSVData, s1, s2):
        if "entity" not in CSVData[0]:
            raise Exception("Entity not gofun in blsalbal")
        positionEntity = CSVData[0].index("entity")
        for i in range(len(CSVData)):
            # print(CSVData[0]) -> la fila entera
            # entity obligatorio:
            print(i)
            if s1 in CSVData[i][positionEntity]:  # Fila entity
                print(CSVData[i])

                #and posicion de esa columna == s1:
                # si estoy en la columna entity y hay un valor == al pasado s1 (p.e. PARIS) imprimir línea
                # print(CSVData[i])

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
