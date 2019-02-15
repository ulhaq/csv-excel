import kkdata
from excel import Excel
from csvalues import Csvalues

class Test:
    def is_xl_and_csv_content_same():
        e = Excel('iris_data.xlsx')
        c = Csvalues('iris_data.csv')

        return e.getContent() == c.getContent()

    def is_csv_and_dict_content_same():
          c = Csvalues('befkbhalderstatkode.csv')
          reader = c.getReader()
          next(reader)

          for row in reader:
              assert kkdata.STATISTICS[row[0]][row[1]][row[2]][row[3]] == row[4]

Test.is_xl_and_csv_content_same()
Test.is_csv_and_dict_content_same()
