def main():
    average = calc_average()
    determine_grade(average)


def calc_average():
    print("Please input your scores out of 100.")
    score1 = input("Test One Score: ")
    score2 = input("Test Two Score: ")
    score3 = input("Test Three Score: ")
    score4 = input("Test Four Score: ")
    score5 = input("Test Five Score: ")
    average = (float(score1) + float(score2) + float(score3) + float(score4) + float(score5)) / 5
    return average


def determine_grade(score):
    print(score)
    if float(score) >= 90:
            print("You got an A! The only grade that matters, according to jerks!!")
    elif float(score) < 90 and score >= 80:
            print("You got a B! Plenty good, means you're still learning!")
    elif float(score) < 80 and score >= 70:
            print("You got a C! Well! Sure!")
    elif float(score) < 70 and score >= 60:
            print("You got a D! Maybe, uh, school better!")
    elif float(score) < 60:
            print("You got an F! If you find a good enough marker, that's a pretty easy B to fake!")


main()
