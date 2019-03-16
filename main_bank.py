# import modules
import csv
import os

# set the file path so its compatible with all operating systems
csvpath = os.path.join(".", "budget_data.csv")

# initialize variables
profitlosscounter = 0
monthcounter = 0
revenue = []
dates = []
revenuechanges = []
totalchange = 0
greatestprofitincrease = 0
greatestprofitloss = 0
greatestincreasedate = ""
greatestlossdate =""

# open the csv file, make it readable, and skip the header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)

# establish the number of  months in the data, the total profit/loss, and create some series
    for row in csvreader:
        monthcounter += 1
        profitlosscounter += int(row[1])
        revenue.append(int(row[1]))
        dates.append(row[0])

# establish the month over month revenue differences
    for x in range(1,len(revenue)):
        revenuechanges.append(revenue[x] - revenue[x-1])

# establish the sum of all month over month revenue differenes
    for x in revenuechanges:
        totalchange = totalchange + x

# store the highest and lowest revenue change values and the date of these changes
    for x in revenuechanges:
        if x > greatestprofitincrease:
            greatestprofitincrease = x
            p = revenuechanges.index(x)
            greatestincreasedate = dates[p+1]
        if x < greatestprofitloss:
            greatestprofitloss = x
            m = revenuechanges.index(x)
            greatestlossdate = dates[m+1]

# calculate the average change
    averagechange = totalchange / len(revenuechanges)

# set variables to print
a = "Financial Analysis "
b = "-------------------- "
c = "Total Months: " + str(monthcounter) + " "
d = "Total: $" + str(profitlosscounter) + " "
e = "Average Change: $" + str(round(averagechange,2)) + " "
f = f"Greatest Increase in Profits: {greatestincreasedate} ${greatestprofitincrease} "
g = f"Greatest Decrease in Profits: {greatestlossdate} ${greatestprofitloss}"

total_print = [a,b,c,d,e,f,g]

print("\n".join(total_print))

# create a txt file with the results
final_path = os.path.join(".", "financial_analysis.txt")
with open(final_path, "w", newline="") as txtfile:
    txtfile.writelines(total_print)

# create a csv file with the results
# output_path = os.path.join(".", "final_financial_analysis.csv")
# with open(output_path, "w", newline="") as csvfile:
#     csvwriter = csv.writer(csvfile)
#     for item in total_print:
#         csvwriter.writerow([item])