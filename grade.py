def main():
    determine_grade()


def calc_average():
    score1 = input("Test One Score: ")
    score2 = input("Test Two Score: ")
    score3 = input("Test Three Score: ")
    score4 = input("Test Four Score: ")
    score5 = input("Test Five Score: ")
    average = score1 + score2 + score3 + score4 + score5
    return average


def determine_grade():
    score = calc_average()
    if score >= 90:
            print("You got an A! The only grade that matters, according to jerks!!")
    elif score < 90 >= 80:
            print("You got a B! Plenty good, means you're still learning!")
    elif score < 80 >= 70:
            print("You got a C! Well! Sure!")
    elif score < 70 >= 60:
            print("You got a D! Maybe, uh, school better!")
    elif score < 60:
            print("You got an F! If you find a good enough marker, that's a pretty easy B to fake!")


main()
