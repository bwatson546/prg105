def main():
    names = open("names.txt", "r")
    count = 0
    names_read = names.readline()
    names_read = names_read.rstrip("\n")

    while names_read != "":
        print(names_read)
        count += 1
        names_read = names.readline()
        names_read = names_read.rstrip("\n")
    names.close()
    print(count, "names in the list")

main()
