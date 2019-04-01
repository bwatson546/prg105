def main():
    split()

def split():
    name=input("Please enter your full name, first middle last:")
    name_list=name.split()
    first=name_list[0]
    middle=name_list[1]
    last=name_list[2]
    first=first[0]
    middle=middle[0]
    last=last[0]
    print(first.upper()+'.'+middle.upper()+'.'+last.upper()+'.')

main()
