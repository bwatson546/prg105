#  set base class
class Question:
    def __init__(self, question, a1, a2, a3, a4, answer):
        self.__question = question
        self.__a1 = a1
        self.__a2 = a2
        self.__a3 = a3
        self.__a4 = a4
        self.__answer = answer

#  create questions and answers
    def set_question(self, question):
        self.__question = question

    def set_a1(self, a1):
        self.__a1 = a1

    def set_a2(self, a2):
        self.__a2 = a2

    def set_a3(self, a3):
        self.__a3 = a3

    def set_a4(self, a4):
        self.__a4 = a4

    def set_answer(self, answer):
        self.__answer = answer

    def get_question(self):
        return self.__question

    def get_a1(self):
        return self.__a1

    def get_a2(self):
        return self.__a2

    def get_a3(self):
        return self.__a3

    def get_a4(self):
        return self.__a4

    def get_answer(self):
        return self.__answer


def main():
    q1 = Question("What class starts in Limsa Lominsa?", "1. Gladiator", "2. Arcanist", "3. Pugilist", "4. Conjurer", "2")

    q2 = Question("Who is the main antagonist of the 2.0 (A Realm Reborn) story?", "1. Thancred", "2. Mistbeard", "3. Sephiroth", "4. Lahabrea", "4")

    q3 = Question("What town contains A Realm Reborn's Relic quests, A Relic Reborn?", "1. Aleport", "2. Hyrstmill", "3. Quarrymill", "4. Black Brush Station", "2")

    q4 = Question("Which major character gets possessed by an Ascian in A Realm Reborn?", "1. Thancred", "2. Minfillia", "3. Mother Miounne", "4. Jihli Aliapoh", "1")

    q5 = Question("Which of these is the Dark Knight's stun move from before Stormblood's Job overhauls?", "1. Shield Bash", "2. Living Dead", "3. Low Blow", "4. Hellsguard", "3")

    q6 = Question("Which Job evolves from Archer?", "1. Bard", "2. Paladin", "3. Red Mage", "4. Dancer", "1")

    q7 = Question("Which of these Jobs is currently not confirmed to be in the game?", "1. Dancer", "2. Paladin", "3. Arithmetician", "4. Summoner", "3")

    q8 = Question("Who is the leader of the Scions of the Seventh Dawn in A Realm Reborn?", "1. Minfillia", "2. F'lhaminn", "3. Hoary Boulder", "4. Careless Whisper", "1")

    q9 = Question("Which of these is not a main arm currently used in the game?", "1. Bow", "2. Cane", "3. Hammer", "4. Needle", "3")

    q10 = Question("Which of these classes did not exist in the original Final Fantasy XIV, before A Realm Reborn?", "1. Arcanist", "2. Thaumaturge", "3. Gladiator", "4. Sentinel", "1")

    player1 = 0  # P1 score
    player2 = 0  # P2 score

    set_1 = [q1, q2, q3, q4, q5]
    set_2 = [q6, q7, q8, q9, q10]

    print("Player 1: ")
    for query in set_1:
        print()
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Enter the number of your choice.")
        if guess == query.get_answer():
            print("Correct!")
            player1 += 1
        else:
            print("Incorrect!")

    print("Player 1 earned: " + str(player1) + "points!")

    print("Player 2: ")
    for query in set_2:
        print()
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Enter the number of your choice.")
        if guess == query.get_answer():
            print("Correct!")
            player2 += 1
        else:
            print("Incorrect!")

    print("Player 2 earned: " + str(player1) + " points!")
    print()
    print("Player 1 earned " + str(player1) + " points!")
    print("Player 2 earned " + str(player2) + " points!")

    if player1 > player2:
        print("Player 1 wins! May you ever walk in the light of the crystal!")
    elif player1 < player2:
        print("Player 2 wins! May you ever walk in the light of the crystal!")
    elif player1 == player2 and player1 > 2:
        print("It's a tie! Warriors of Light, all!")
    elif player1 == player2 and player1 < 2:
        print("It's a tie! Go buy a lorebook, both of you!")


main()
