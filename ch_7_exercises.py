"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 7.2 Lists
print("=" * 10, "Section 7.2 lists", "=" * 10)
# 1) Create a list of days of the week, assign it to the variable days, remove """ """ to test


days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


# 2) Create a list with 5 items, set them all to 0, use the Repetition Operator ( * )

zero = [0] * 5

# 3) Print the contents of your days list using the for operator

for x in days:
    print(x)

# 4) Print the list item that holds the value Saturday from the days list by using it's index

print(days.index("Saturday"))

# 5) Create a variable called size to hold the length of the list days using the len function

length = len(days)
print(length)

# 6) Concatenate the two following lists together, storing the value in list3 - remove the """ """ to test


list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = list1 + list2
print(list3)


# TODO 7.3 List Slicing
print("=" * 10, "Section 7.3 list slicing", "=" * 10)
# Slice the list days to select from Monday through Friday, inclusive, and assign the new list to work_days
# Print work_days



# TODO 7.4 Finding items in Lists with the in Operator
print("=" * 10, "Section 7.4 using the in operator", "=" * 10)
# Test to see if "Tue" is in the list days - display "yes, Tue is in the list" or "no, Tue is not in the list"

if "Tue" in days:
    print("Yes, Tue is in the list")
else:
    print("No, Tue is not in the list")

# TODO 7.5 List Methods and Useful Built-in Functions
print("=" * 10, "Section 7.5 list methods and functions", "=" * 10)
# 1) Use append() to append the last three months of the year to the list months.
months = list(["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept"])

months.append("Oct")
months.append("Nov")
months.append("Dec")


# 2) Get the index of "May" from the months list and print it on screen

index = months.index("May")
print(index)

# 3) Sort list3 from exercise 7.2 and print the results on screen

list3.sort()
print(list3)

# 4) Reverse the order of list3

list3.reverse()

# 5) Delete the number 5 from list3 and print the list(remember we reversed the list)

list3.remove(5)
print(list3)

# 6) Print the maximum value from list 3

print(max(list3))

# TODO 7.6 Copying Lists
print("=" * 10, "Section 7.6 copying lists", "=" * 10)
# Copy the list months to the variable months_of_the_year
# Print the values in months_of_the_year

months_of_the_year = months
print(months_of_the_year)

# TODO 7.7 Processing lists
print("=" * 10, "Section 7.7 processing lists", "=" * 10)
# 1) Total the values in list3 and print the results

total = sum(list3)
print(total)

#  or print(sum(list3))
total = 0
count = 0
for x in list3:
    total += x
    count += 1
print(total)

# 2) Get the average of values in list3 and print the results

count = list3.count

average = total/len(list3)
print(average)

# 3) Open the file states.txt in read mode,
# -- read the contents of the file into the list states_list
# -- print the contents of states_list on screen

states_list = []
states = open("States.txt", "r")
nextline = states.readline()
while nextline != "":
    states_list.append(nextline.rstrip('\n'))
    nextline = states.readline()

print(states_list)
states.close()

# TODO 7.8 Two-Dimensional Lists
print("=" * 10, "Section 7.8 two-dimensional lists", "=" * 10)
# 1) Create a new two dimensional list that has the months of the year
#     and the days in each month during a non leap year
#     For example, the first entry should be: January, 31

calendar = [["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"],[31,28,31,30,31,30,31,31,30,31,30,31]]

# 2) Print the contents of the entire list

print(calendar[0:12][0])
print(calendar[0:12][1])

# 3) Print just the values for index 3,0 and 3,1

print(calendar[0][3])
print(calendar[1][3])

# TODO 7.9 Tuples
print("=" * 10, "Section 7.9 tuples", "=" * 10)
# Create a tuple using the months list as its data source

calenTuple = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]

print(calenTuple)
