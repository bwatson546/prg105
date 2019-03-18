def main():
    numlist = open("numbers.txt", "r")
    count = 0
    numtot = 0
    num_read = numlist.readline()
    num_read = num_read.rstrip("\n")

    while num_read != "":
        number = int(num_read)
        print(num_read)
        count += 1
        num_read = numlist.readline()
        num_read = num_read.rstrip("\n")
        numtot = numtot + number
    numlist.close()
    print(count, "numbers in the list")
    print("The total of your numbers is:", numtot)
    print("The average of your numbers is:", format(numtot/count, '.2f'))


main()
