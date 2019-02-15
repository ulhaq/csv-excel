import csv

class Csvalues:
    def __init__(self, filename='iris_data.csv'):
        self.filename = filename

    def getReader(self):
        file = open(self.filename, 'r')

        return csv.reader(file)

    def getWriter(self):
        file = open(self.filename, 'w', newline=None)

        return csv.writer(file)

    def getColumn(self, pos = 1):
        list = []
        for i in range(1, self.getTotalRows()):
            cell = self.getActiveSheet().cell(row = i, column = pos)
            list.append(cell.value)
        return list

    def getFirstRow(self):
        return next(self.getReader())

    def getContent(self):
        list = []

        for row in self.getReader():
            list.append(row)
        return list
