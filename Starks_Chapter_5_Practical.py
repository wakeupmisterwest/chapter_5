import csv
# Pull in the CSV file
filename = 'candy_type.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
        # Loop through the csv file and create two lists
    candy_type = []
    candy_price = []
    candy_duplicate = {}
    def sum_numbers(numbers):
        total = 0
        for number in numbers:
            total += number
        return total

    for row in reader:
        candy = row[1]
        price = float(row[2])
        candy_type.append(candy)
        candy_price.append(price)
        candy_type.sort()
        candy_price.sort()
    print(candy_type)
    print(candy_price)

for candy in candy_type:
    candy_duplicate[candy] = candy_duplicate.get(candy, 0) + 1
candy_duplicate = [candy for candy, count in candy_duplicate.items() if count
                   > 1]

for candy in candy_duplicate:
    print(f"{candy} have been duplicated.")

print(f"The total cost is {round(sum_numbers(candy_price))}")

candy_price = [candy for candy in candy_price if candy < 3]

print(candy_price)

print(f"The new total cost is {round(sum_numbers(candy_price))}")

walmart_price = [1.30, 1.97, 1.47, 1.32]

for item in candy_type[23:]:
    if item == 'Twix':
        print(f"{item} costs {walmart_price[0]} at Walmart")
    if item == 'cookie n cream Hershey king size bar ':
        print(f"{item}costs {walmart_price[0]} at Walmart")
    if item == 'heath bar':
        print(f"{item} costs {walmart_price[1]} at Walmart")
    if item == 'mints':
        print(f"{item} costs {walmart_price[2]} at Walmart")
    if item == 'reeces':
        print(f"{item} costs {walmart_price[3]} at Walmart")

print(f"The total cost at Walmart is {round(sum_numbers(walmart_price))}")
