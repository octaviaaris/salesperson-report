"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

# salespeople = []
# melons_sold = []

# f = open("sales-report.txt")    # open file
# for line in f:                  # iterate through lines in file
#     line = line.rstrip()        # strip each line of trailing whitespace
#     entries = line.split("|")   # split each line by | and bind list to entries
#     salesperson = entries[0]    # set 0th item (salesperson name) to salesperson
#     melons = int(entries[2])    # turn 2nd item (number of melons) to integer and assign to melons

#     if salesperson in salespeople:                  # if salesperson is in salespeople
#         position = salespeople.index(salesperson)   # sets position to lowest index at which salesperson is found
#         melons_sold[position] += melons             # adds melons to subtotal for melons_sold
#     else:                                           # if salesperson not in salespeople
#         salespeople.append(salesperson)             # add salesperson to salespeople
#         melons_sold.append(melons)                  # add melons_sold to melons


# for i in range(len(salespeople)):                   # iterate through salespeople
#     print "{} sold {} melons".format(salespeople[i], melons_sold[i])    # print salesperson and melons_sold at index i

# created dictionary containing {salesperson: melons_sold} value pairs
# instead of two separate lists

sales_info = {}

with open("sales-report.txt") as f:
    for line in f:
        line = line.rstrip()
        entries = line.split("|")
        salesperson = entries[0]
        melons = int(entries[2])

        if salesperson in sales_info:
            sales_info[salesperson] += melons
        else:
            sales_info[salesperson] = melons

for name, num_sold in sales_info.iteritems():
    print "{} sold {} melons".format(name, num_sold)
