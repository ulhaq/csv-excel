from csvalues import Csvalues

def csvToDict(csv_name, output_name):
    c = Csvalues(csv_name)
    reader = c.getReader()
    next(reader)
    dict = {}

    for row in reader:
        if not row[0] in dict:
            dict[row[0]] = {}
        if not row[1] in dict[row[0]]:
            dict[row[0]][row[1]] = {}
        if not row[2] in dict[row[0]][row[1]]:
            dict[row[0]][row[1]][row[2]] = {}

        dict[row[0]][row[1]][row[2]][row[3]] = row[4]

    f = open(output_name, 'w')
    f.write("STATISTICS = " + str(dict))
    f.close()

    print("The CSV was converted to Dictionary successfully")

    return
