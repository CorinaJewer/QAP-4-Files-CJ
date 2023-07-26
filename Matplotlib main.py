# Comment: Graph of total sales for each month of the year. Months may be null if business started or ended part way
# through the calendar year.
# Written By Corina Jewer
# Date: July 25, 2023

# Libraries

import matplotlib.pyplot as plt
import matplotlib as style

# Defaults/Constants

# Functions


# Main Program

Months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
SalesData = []
for Month in Months:
    while True:
        try:
            MonthlySales = float(input(f"Enter the total sales for {Month}: "))
            if MonthlySales < 0:
                print("Sales value cannot be negative. Please enter a valid amount.")
            else:
                SalesData.append(MonthlySales)
                break
        except ValueError:
            print("Please enter a valid number for the total monthly sales.")

fig, ax = plt.subplots()

ax.bar(Months, SalesData, align='center', color='orange', edgecolor='black')

ax.set_title('Sales Data Per Month')
ax.set_ylabel('Sales ($)')
ax.set_xlabel('Months')

ax.set_xticks(Months)
ax.set_xticklabels(Months)

plt.show()
