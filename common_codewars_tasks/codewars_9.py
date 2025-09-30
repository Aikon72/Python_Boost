# https://www.codewars.com/kata/59d727d40e8c9dd2dd00009f/train/python

# You are given a (small) check book as a - sometimes - cluttered (by non-alphanumeric characters) string:
#
# "1000.00
# 125 Market 125.45
# 126 Hardware 34.95
# 127 Video 7.45
# 128 Book 14.32
# 129 Gasoline 16.10"
# The first line shows the original balance. Each other line (when not blank) gives information: check number, category, check amount. (Input form may change depending on the language).
#
# First you have to clean the lines keeping only letters, digits, dots and spaces.
#
# Then return a report as a string (underscores show spaces -- don't put them in your solution. They are there so you can see them and how many of them you need to have):
#
# "Original_Balance:_1000.00
# 125_Market_125.45_Balance_874.55
# 126_Hardware_34.95_Balance_839.60
# 127_Video_7.45_Balance_832.15
# 128_Book_14.32_Balance_817.83
# 129_Gasoline_16.10_Balance_801.73
# Total_expense__198.27
# Average_expense__39.65"
# On each line of the report you have to add the new balance and then in the last two lines the total expense and the average expense. So as not to have a too long result string we don't ask for a properly formatted result.
#
# Notes
# See input examples in Sample Tests.
# It may happen that one (or more) line(s) is (are) blank.
# Round to 2 decimals your calculated results (Elm: without traling 0)
# The line separator of results may depend on the language \n or \r\n. See examples in the "Sample tests".


def balance(book):
    book = book.split("\n")
    temp = ""
    for c in book[0]:
        if c.isdigit() or c == ".":
            temp += c
    total = float(temp)
    answer = "Original Balance: " + f"{total:.2f}" + "\r\n"
    del book[0]
    counter = 0
    expenses = 0
    for line in book:
        sub_line = ""
        for c in line:
            if c.isdigit() or c.isalpha() or c in (" ", "."):
                sub_line += c
        if sub_line == "":
            continue
        #print(sub_line)
        sub_sum = float(sub_line.split()[2])
        sub_line_tiles = sub_line.split()
        total -= sub_sum
        answer += sub_line_tiles[0] + " "+ sub_line_tiles[1] + " " + f"{float(sub_line_tiles[2]):.2f}" +f" Balance {total:.2f}\r\n"
        expenses = round(expenses + sub_sum, 2)
        counter += 1
    aver_exp = expenses/counter
    answer += f"Total expense  {expenses:.2f}\r\nAverage expense  {aver_exp:.2f}"

    return answer



b1 = """1000.00!=

125 Market !=:125.45
126 Hardware =34.95
127 Video! 7.45
128 Book :14.32
129 Gasoline ::16.10
"""


b2 = """1233.00
125 Hardware;! 24.8?;
123 Flowers 93.5
127 Meat 120.90
120 Picture 34.00
124 Gasoline 11.00
123 Photos;! 71.4?;
122 Picture 93.5
132 Tyres;! 19.00,?;
129 Stamps 13.6
129 Fruits{} 17.6
129 Market;! 128.00?;
121 Gasoline;! 13.6?;"""

print(balance(b1))
print(balance(b2))

