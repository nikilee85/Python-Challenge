import csv

with open("budget_data.csv") as csv_file:

    budget = next(csv.reader(csv_file))

    readercount = 0
    total = 0
    totalChange = 0
    currentVal = 0
    firstRun = 1
    amountChange = 0
    greatestInc = 0
    greatestDec = 0

    for row in csv.reader(csv_file):
        total += int(row[1])
        if firstRun == 1:
            currentVal = int(row[1])
            firstRun = 0
            readercount += 1
        else:
            currentChange = int(row[1]) - currentVal
            totalChange += currentChange
            currentVal = int(row[1])
            amountChange += 1
            readercount += 1
            if currentChange > greatestInc:
                greatestInc = currentChange
                giMonth = row[0]
            if currentChange < greatestDec:
                greatestDec = currentChange
                gdMonth = row[0]


    print("Total Months: " + str(readercount))
    print("Profit/Losses:" + "$" + str(total))
    print("averageChange:" + "$" + str(totalChange/(amountChange)))
    print("Greatest Increase: " + giMonth + " $" + str(greatestInc))
    print("Greatest Decrease: " + gdMonth + " $" + str(greatestDec))

with open("budget_data.txt",'w') as f:
    print("Total Months: " + str(readercount),file=f)
    print("Profit/Losses:" + "$" + str(total),file=f)
    print("averageChange:" + "$" + str(totalChange/(amountChange)),file=f)
    print("Greatest Increase: " + giMonth + " $" + str(greatestInc),file=f)
    print("Greatest Decrease: " + gdMonth + " $" + str(greatestDec),file=f)